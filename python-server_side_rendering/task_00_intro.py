def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"
        with open(filename, "w") as file:
            file.write(output)
