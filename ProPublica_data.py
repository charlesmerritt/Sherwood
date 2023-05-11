from main import *
import json
# Set up the API endpoint and headers
api_endpoint_senate = "https://api.propublica.org/congress/v1/117/senate/members.json"
api_endpoint_house = "https://api.propublica.org/congress/v1/117/house/members.json"
api_headers = {"X-API-Key": PROPUBLICA}

# Make the API request
response_senate = requests.get(api_endpoint_senate, headers=api_headers)
response_house = requests.get(api_endpoint_house, headers=api_headers)

# Check if the request was successful
if response_senate.status_code == 200:
    # Retrieve the data from the API response
    data = response_senate.json()

    # Extract the data for each member of Congress
    members = data["results"][0]["members"]

    # Save the member data as a JSON file
    with open("member_senate_data.json", "w") as outfile:
        json.dump(members, outfile, indent=4)

    # Print a message indicating that the data was
    print("This is from session 2021/1/3 - 2023/1/3")
    print("Member data saved to member_senate_data.json")

    # Print the number of members in the Senate
    num_members = len(members)
    print(f"Number of members in the Senate: {num_members}")

else:
    print(f"Error: {response_senate.status_code}")

if response_house.status_code == 200:
    # Retrieve the data from the API response
    data = response_house.json()

    # Extract the data for each member of Congress
    members = data["results"][0]["members"]

    # Save the member data as a JSON file
    with open("member_house_data.json", "w") as outfile:
        json.dump(members, outfile, indent=4)

    # Print a message indicating that the data was
    print("Member data saved to member_house_data.json")

    # Print the number of members in the Senate
    num_members = len(members)
    print(f"Number of members in the House: {num_members}")
else:
    # Handle errors, such as logging the error or raising an exception
    print(f"Error: {response_house.status_code}")
