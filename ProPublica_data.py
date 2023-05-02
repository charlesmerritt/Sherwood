from main import *
# Set up the API endpoint and headers
api_endpoint = "https://api.propublica.org/congress/v1/116/senate/members.json"
api_headers = {"X-API-Key": PROPUBLICA}

# Make the API request
response = requests.get(api_endpoint, headers=api_headers)

# Check if the request was successful
if response.status_code == 200:
    # Retrieve the data from the API response
    data = response.json()

    # Extract the data for each member of Congress
    members = data["results"][0]["members"]

    # Save the member data as a JSON file
    with open("member_data.json", "w") as outfile:
        json.dump(members, outfile, indent=4)

    # Print a message indicating that the data was
    print("Member data saved to member_data.json")
else:
    # Handle errors, such as logging the error or raising an exception
    print(f"Error: {response.status_code}")
