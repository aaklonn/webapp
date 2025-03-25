import csv
import random
from flask import Flask, request, jsonify, render_template
import pandas as pd
import traceback

from old import old_bp

app = Flask(__name__)

app.register_blueprint(old_bp)


@app.route('/iit')
def iit_predictor():
    return render_template('iit_predictor.html')

    
    # Inflation factor based on expected increase in candidates
    inflation_factor = 1.097  # 9.7% increase
    
    # Category-wise total candidates (from 0 percentile data)
    category_totals = {
        'OPEN': 1408702,  # From open.csv last rank
        'OBC': 575820,    # From obc.csv last rank
        'SC': 138542,     # From sc.csv last rank
        'ST': 46818,      # From st.csv last rank
        'EWS': 170469,    # From ews.csv last rank
        'OPEN-PWD': 4316,  # From openpwd.csv last rank
        'OBC-PWD': 1953,  # From obcpwd.csv last rank
        'SC-PWD': 377,    # From scpwd.csv last rank
        'ST-PWD': 107,    # From stpwd.csv last rank
        'EWS-PWD': 535    # From ewspwd.csv last rank
    }
    
    # Apply inflation to category totals
    inflated_totals = {cat: int(total * inflation_factor) for cat, total in category_totals.items()}
    
    try:
        # Read the appropriate CSV file based on category
        filename = {
            'OPEN': 'open.csv',
            'OBC': 'obc.csv',
            'SC': 'sc.csv',
            'ST': 'st.csv',
            'EWS': 'ews.csv',
            'OPEN-PWD': 'openpwd.csv',
            'EWS-PWD': 'ewspwd.csv',
            'OBC-PWD': 'obcpwd.csv',
            'SC-PWD': 'scpwd.csv',
            'ST-PWD': 'stpwd.csv'
        }.get(category)
        
        if not filename:
            return jsonify({'error': 'Invalid category'}), 400
        
        # Adjust rank based on inflation
        adjusted_rank = int(rank / inflation_factor)
        
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            # Convert data to list of tuples (rank, percentile)
            data_points = []
            for line in lines:
                r, p = line.strip().split(',')
                r = int(r.replace(',', ''))  # Remove commas from rank
                p = float(p)
                data_points.append((r, p))
            
            # Sort by rank
            data_points.sort(key=lambda x: x[0])
            
            # Find closest ranks and interpolate
            for i in range(len(data_points) - 1):
                if data_points[i][0] <= adjusted_rank <= data_points[i + 1][0]:
                    rank1, perc1 = data_points[i]
                    rank2, perc2 = data_points[i + 1]
                    
                    # Linear interpolation
                    percentile = perc1 + (adjusted_rank - rank1) * (perc2 - perc1) / (rank2 - rank1)
                    
                    return jsonify({
                        'rank': rank,
                        'adjusted_rank': adjusted_rank,
                        'percentile': round(percentile, 2),
                        'category': category,
                        'total_candidates': inflated_totals[category]
                    })
            
            # If rank is beyond the last rank in data
            if adjusted_rank > data_points[-1][0]:
                return jsonify({
                    'rank': rank,
                    'adjusted_rank': adjusted_rank,
                    'percentile': 0,
                    'category': category,
                    'total_candidates': int(total_candidates * 1.097),
                    'total_candidates': inflated_totals[category]
                })
            
            # If rank is before the first rank in data
            if adjusted_rank < data_points[0][0]:
                return jsonify({
                    'rank': rank,
                    'adjusted_rank': adjusted_rank,
                    'percentile': 100,
                    'category': category,
                    'total_candidates': inflated_totals[category]
                })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_rank', methods=['POST'])
def predict_rank():
    try:
        data = request.get_json()
        percentile = float(data.get('percentile'))
        category = data.get('category')
        
        if not percentile or not category:
            return jsonify({'error': 'Missing required fields'}), 400
            
        if percentile < 0 or percentile > 100:
            return jsonify({'error': 'Percentile must be between 0 and 100'}), 400
            
        # Category-wise total candidates (2023 data)
        category_totals = {
            'OPEN': 1408702,
            'EWS': 170469,
            'OBC': 575820,
            'SC': 138542,
            'ST': 46818,
            'OPEN-PWD': 4316,
            'EWS-PWD': 535,
            'OBC-PWD': 1953,
            'SC-PWD': 377,
            'ST-PWD': 107
        }
        
        # Apply inflation factor (9.7% increase)
        inflation_factor = 1.097
        total_candidates = int(category_totals[category] * inflation_factor)
        
        # Map category to CSV filename
        csv_files = {
            'OPEN': 'open.csv',
            'EWS': 'ews.csv',
            'OBC': 'obc.csv',
            'SC': 'sc.csv',
            'ST': 'st.csv',
            'OPEN-PWD': 'openpwd.csv',
            'EWS-PWD': 'ewspwd.csv',
            'OBC-PWD': 'obcpwd.csv',
            'SC-PWD': 'scpwd.csv',
            'ST-PWD': 'stpwd.csv'
        }
        
        csv_file = csv_files.get(category)
        if not csv_file:
            return jsonify({'error': 'Invalid category'}), 400
        
        # Read CSV file and convert to list of tuples (rank, percentile)
        data_points = []
        with open(csv_file, 'r') as f:
            for line in f:
                rank, perc = line.strip().split(',')
                rank = int(rank.replace(',', ''))  # Remove commas from rank
                perc = float(perc)
                data_points.append((rank, perc))
        
        # Sort by percentile in descending order (highest percentile first)
        data_points.sort(key=lambda x: x[1], reverse=True)
        
        # If percentile is higher than the highest in data, return 1
        if percentile >= data_points[0][1]:
            return jsonify({
                'rank': 1,
                'last_year_rank': 1,
                'last_year_candidates': total_candidates,
                'total_candidates': int(total_candidates * 1.097),
                'percentile': percentile,
                'category': category
            })
            
        # If percentile is lower than the lowest in data, return total candidates
        if percentile <= data_points[-1][1]:
            return jsonify({
                'rank': total_candidates,
                'last_year_rank': category_totals[category],
                'last_year_candidates': total_candidates,
                'total_candidates': int(total_candidates * 1.097),
                'percentile': percentile,
                'category': category
            })
            
        # Find the two points to interpolate between
        for i in range(len(data_points) - 1):
            if data_points[i][1] >= percentile >= data_points[i + 1][1]:
                r1, p1 = data_points[i]
                r2, p2 = data_points[i + 1]
                
                # Linear interpolation for last year's rank
                last_year_rank = r1 + (r2 - r1) * (percentile - p1) / (p2 - p1)
                last_year_rank = int(last_year_rank)
                
                # Apply inflation factor to get this year's predicted rank
                predicted_rank = int(last_year_rank * inflation_factor)
                
                return jsonify({
                    'rank': predicted_rank,
                    'last_year_rank': last_year_rank,
                    'last_year_candidates': total_candidates,
                    'total_candidates': int(total_candidates * 1.097),
                    'percentile': percentile,
                    'category': category
                })
        
        # If we get here, something went wrong with the interpolation
        return jsonify({'error': 'Failed to interpolate rank'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_iit', methods=['POST'])
def predict_iit():
    data = request.json
    
    if data is None:
        print("No JSON data received")
        return jsonify({'error': 'No JSON data received'}), 400
    
    # Print data for debugging
    print(f"Received data: {data}")
    
    rank = data.get('rank')
    category = data.get('category')
    gender = data.get('gender')
    college_names = data.get('colleges', ['ALL'])
    branch_names = data.get('branches', ['ALL'])
    seat_filter = data.get('seat_filter', 'all')  # Get seat filter preference
    
    # Print values for debugging
    print(f"Processing request: rank={rank}, category={category}, gender={gender}, seat_filter={seat_filter}")
    print(f"Colleges: {college_names}")
    print(f"Branches: {branch_names}")
    
    if None in (rank, category, gender):
        print("Missing required fields")
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        rank = int(rank)
        # Allow for ranks up to 3% worse than closing rank
        max_rank = int(rank * 1.03)
        
        results_2023 = []
        results_2024 = []
        
        # Process each college
        for college_name in college_names:
            for branch_name in branch_names:
                # Process 2024 data
                results = process_iit_data({
                    'quota': 'OPEN',
                    'category': category,
                    'gender': gender,
                    'college': college_name,
                    'branch': branch_name,
                    'collegename': college_name,
                    'max_rank': max_rank,  # Pass the max rank to consider
                    'year': '2024',
                    'csv_file': 'iit2024.csv',
                    'user_rank': rank  # Add user's rank
                })
                
                for result in results:
                    try:
                        closing_rank = int(result['Closing Rank'])
                        result['Probability'] = calculate_probability(rank, closing_rank)
                        # Only add if not "Not Eligible"
                        if result['Probability'] != "Not Eligible":
                            results_2024.append(result)
                    except ValueError as ve:
                        print(f"Error processing result: {ve}")
                        continue
                    
                # Process 2023 data
                results = process_iit_data({
                    'quota': 'OPEN',
                    'category': category,
                    'gender': gender,
                    'college': college_name,
                    'branch': branch_name,
                    'collegename': college_name,
                    'max_rank': max_rank,  # Pass the max rank to consider
                    'year': '2023',
                    'csv_file': 'iit2023.csv',
                    'user_rank': rank  # Add user's rank
                })
                
                for result in results:
                    try:
                        closing_rank = int(result['Closing Rank'])
                        result['Probability'] = calculate_probability(rank, closing_rank)
                        # Only add if not "Not Eligible"
                        if result['Probability'] != "Not Eligible":
                            results_2023.append(result)
                    except ValueError as ve:
                        print(f"Error processing result: {ve}")
                        continue
                
        # Combine results from both years
        combined_results = combine_results(results_2023, results_2024, rank)
        
        # Filter by seat type if specified
        if seat_filter != 'all':
            if seat_filter == 'female':
                combined_results = [r for r in combined_results if r['SeatType'] == 'Female-Only']
            elif seat_filter == 'neutral':
                combined_results = [r for r in combined_results if r['SeatType'] == 'Gender Neutral']
        elif gender == "FEMALE":
            # For female candidates, ensure unique college-branch combinations
            # when showing both seat types
            unique_entries = {}
            for result in combined_results:
                key = (result['College'], result['Branch'], result['Category'])
                # If we already have this college-branch combo, only replace if better probability
                if key in unique_entries:
                    existing_prob = unique_entries[key]['Probability']
                    new_prob = result['Probability']
                    # Compare probabilities (Very High > High > Medium > Low > Very Low)
                    prob_rank = {"Very High": 5, "High": 4, "Medium": 3, "Low": 2, "Very Low": 1}
                    if prob_rank.get(new_prob, 0) > prob_rank.get(existing_prob, 0):
                        unique_entries[key] = result
                else:
                    unique_entries[key] = result
            
            # Replace combined_results with the unique entries
            combined_results = list(unique_entries.values())
        
        return jsonify(combined_results)
        
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

def process_iit_data(data):
    results = []
    try:
        with open(data['csv_file'], "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 7:
                    continue
                
                college_name = row[0]
                branch_name = row[1]
                quota = row[2]  # Should be "AI"
                cat = row[3]    # Category from CSV
                seat_type = row[4]  # "Neutral" or "Female" in CSV
                opening_rank_val = int(row[5])
                closing_rank_val = int(row[6])
                
                # Skip if category doesn't match
                if cat != data['category']:
                    continue
                
                # Skip if rank is higher than max allowed rank
                user_rank = data['user_rank']  # Use user_rank instead of rank
                max_rank = data['max_rank']
                if user_rank > max_rank:
                    continue
                
                # Filter by college and branch if specified
                if data['college'] != "ALL" and college_name not in data['college']:
                        continue
                if data['branch'] != "ALL" and branch_name not in data['branch']:
                        continue
                
                # Handle gender-based seat type filtering
                if data['gender'] == "MALE":
                    if seat_type != "Neutral":  # Exact match with CSV value
                        continue
                elif data['gender'] == "FEMALE":
                    if seat_type not in ["Neutral", "Female"]:  # Accept both for females
                        continue
                
                results.append({
                            "College": college_name,
                            "Branch": branch_name,
                    "Category": cat,
                    "Quota": quota,
                    "Seat Type": "Female-Only" if seat_type == "Female" else "Gender Neutral",
                    "Opening Rank": opening_rank_val,
                    "Closing Rank": closing_rank_val,
                    "Year": data['year']
                })
            
    except Exception as e:
        print(f"Error processing file: {e}")
        traceback.print_exc()
    
    return results

def calculate_probability(rank, closing_rank):
    """
    Calculate probability of admission based on rank and closing rank.
    Returns a text-based probability value.
    
    Very High: rank is 20% or better than closing rank
    High: rank is 10-19% better than closing rank
    Medium: rank is between closing rank and 5% better
    Low: rank is within 1% worse than closing rank
    Very Low: rank is 1-3% worse than closing rank
    """
    if closing_rank == 0:
        return "Very Low"
        
    # For the case where rank is better than closing rank
    if rank <= closing_rank:
        # Calculate how much better the rank is as a percentage
        rank_diff_percent = (closing_rank - rank) / closing_rank * 100
        
        if rank_diff_percent >= 20:
            return "Very High"
        elif rank_diff_percent >= 10:
            return "High"
        else:  # Between closing rank and 10% better
            return "Medium"
    else:
        # For the case where rank is worse than closing rank
        # Calculate how much worse as a percentage
        rank_worse_percent = (rank - closing_rank) / closing_rank * 100
        
        if rank_worse_percent <= 1:
            return "Low"
        elif rank_worse_percent <= 3:
            return "Very Low"
        else:
            return "Not Eligible"

def combine_results(results_2023, results_2024, rank):
    print("Combining results from 2023 and 2024")
    print(f"Input: {len(results_2023)} results from 2023, {len(results_2024)} results from 2024")
    
    combined = []
    seen_combinations = set()
    
    # Process 2024 data first
    for result in results_2024:
        college_branch_category_seat = (result["College"], result["Branch"], result["Category"], result["Seat Type"])
        
        if college_branch_category_seat in seen_combinations:
            continue
            
        seen_combinations.add(college_branch_category_seat)
        
        # Create combined result with all required fields
        combined_result = {
            "College": result["College"],
            "Branch": result["Branch"],
            "Category": result["Category"],
            "Quota": result["Quota"],
            "SeatType": result["Seat Type"],
            "Year": "2024",
            "OpeningRank": result["Opening Rank"],
            "ClosingRank": result["Closing Rank"],
            "Probability": result["Probability"]
        }
        combined.append(combined_result)
    
    # Add 2023 data
    for result in results_2023:
        college_branch_category_seat = (result["College"], result["Branch"], result["Category"], result["Seat Type"])
        
        # Update existing entries with 2023 data
        found = False
        for item in combined:
            if (item["College"], item["Branch"], item["Category"], item["SeatType"]) == college_branch_category_seat:
                # Add 2023 data to existing entry
                item["OpeningRank2023"] = result["Opening Rank"]
                item["ClosingRank2023"] = result["Closing Rank"]
                found = True
                break
        
        # If not found in combined results, add as a new entry
        if not found:
            combined_result = {
                "College": result["College"],
                "Branch": result["Branch"],
                "Category": result["Category"],
                "Quota": result["Quota"],
                "SeatType": result["Seat Type"],
                "Year": "2023",
                "OpeningRank": result["Opening Rank"],
                "ClosingRank": result["Closing Rank"],
                "Probability": "N/A"  # No probability for 2023-only entries
            }
            combined.append(combined_result)
    
    # Sort by probability (text-based)
    def get_probability_score(prob):
        scores = {
            "Very High": 5,
            "High": 4,
            "Medium": 3,
            "Low": 2,
            "Very Low": 1,
            "N/A": 0
        }
        return scores.get(prob, 0)
    
    combined.sort(key=lambda x: (get_probability_score(x["Probability"]), x["College"]), reverse=True)
    
    print(f"Combined results: {len(combined)} entries")
    for result in combined[:2]:  # Print first 2 results as sample
        print(f"Sample result: {result}")
    
    return combined

@app.route('/get_iit_branches', methods=['GET'])
def get_iit_branches():
    gender = request.args.get('gender')
    
    # Even if gender is not provided, still return all branches
    branches = set()
    
    try:
        # Use 2024 data for more up-to-date branch list
        with open("iit2024.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 5:
                    continue
                
                branch_name = row[1]
                
                # Add all branches, regardless of gender/seat type
                branches.add(branch_name)
        
        branch_list = sorted(list(branches))
        print(f"Found {len(branch_list)} unique branches in iit2024.csv")
        print(f"First 5 branches: {branch_list[:5]}")
        
        return jsonify(branch_list)
    
    except Exception as e:
        print(f"Error loading branches: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/get_iit_colleges', methods=['GET'])
def get_iit_colleges():
    colleges = set()
    
    try:
        # Use 2024 data for more up-to-date college list
        with open("iit2024.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                
                college_name = row[0]
                colleges.add(college_name)
        
        # Print for debugging
        print(f"Found {len(colleges)} IIT colleges")
        college_list = sorted(list(colleges))
        print(f"First few colleges: {college_list[:3]}")
        
        return jsonify(college_list)
    
    except Exception as e:
        print(f"Error loading colleges: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/percentile_predictor')
def percentile_predictor():
    return render_template('percentile_predictor.html')

if __name__ == '__main__':
    ran=random.randrange(5000,9999)
    app.run(debug=True , port=ran)
