# Task 1

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# open new service ticket

def openTicket(id, customer_name, issue, status):
    new_ticket_content = {"Customer": customer_name, "Issue": issue, "Status": status}
    service_tickets.update({id: new_ticket_content})
    
# update status
def update_status(id, new_status):
    service_tickets.get(id).update({"Status": new_status})

# display tickets by status or all tickets if filter not passed
def display_tickets(status_filter="none"):
    if status_filter == "open":
        for item in service_tickets.items():
            ticket_content = item[1]
            if ticket_content.get("Status") == "open":
                print(item)
    elif status_filter == "closed":
        for item in service_tickets.items():
            ticket_content = item[1]
            if ticket_content.get("Status") == "closed":
                print(item)
    else:
        for item in service_tickets.items():
            print(item)

# Open 2 new tickets, update status to closed for 2 tickets,
# display tickets filtered by status closed, display all tickets
openTicket("Ticket003", "Candice", "Website crash", "open")
openTicket("Ticket004", "David", "Overcharged payment", "open")
display_tickets()
update_status("Ticket001", "closed")
update_status("Ticket004", "closed")
display_tickets("closed")
display_tickets()