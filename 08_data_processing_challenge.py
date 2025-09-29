#All the inputs
campaign_name = input("Enter campaign name: ")
email_list_input = input("Enter email addresses (comma-separated): ")
engagement_input = input("Enter engagement status for each email (comma-separated): ")
campaign_type = input("Enter campaign type (promotional, newsletter, transactional): ")

#Making the lists easier for the computer
email_list = [email.strip().lower() for email in email_list_input.split(",")]
engagement_list = [status.strip().lower() for status in engagement_input.split(",")]

#If the emain and engagement numbers dont add up its automatically a error
if len(email_list) != len(engagement_list):
    print("Error: The number of emails and engagement statuses doesn't match.")
    exit()  


domain_counts = {}  
engagement_summary = {
    "opened": 0,
    "clicked": 0,
    "bounced": 0,
    "unsubscribed": 0
}

#Calculating the click rate
total_emails = len(email_list)
clicked_emails = engagement_summary["clicked"]
click_rate = (clicked_emails / total_emails) * 100  

#Checking the success rate
if click_rate >= 50:
    success = "Excellent"
elif click_rate >= 30:
    success = "Good"
elif click_rate >= 10:
    success = "Average"
else:
    success = "Poor"

#Printint the domain
for domain in domain_counts:
    print(domain, domain_counts)

#Printing everything
print("Campaign Name:", campaign_name)
print("Campaign Type:", campaign_type)
print("Click Rate:", click_rate )
print("Success =", success )


