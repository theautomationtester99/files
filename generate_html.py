from jinja2 import Environment, FileSystemLoader

# Define your data to populate in the template
data = {
    "page_title": "Test Report",
    "test_description": "Sample test description goes here.",
    "browser_img_src": "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTQgMTQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxsaW5lYXJHcmFkaWVudCBpZD0iYSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIxMjcuNDY5NiIgeDI9IjEyNy40Njk2IiB5MT0iODIuMjU5MjM5IiB5Mj0iMTczLjY2NjQ0Ij48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM4NmJiZTUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMxMDcyYmEiLz48L2xpbmVhckdyYWRpZW50PjxwYXRoIGQ9Im02Ljk4NDc3NjYzIDEuMDAxMDYzMTJzMy41MjQwMDczOS0uMTU4MTQwNTMgNS4zOTIzNTgyNSAzLjM4NDAyMDI2aC01LjY5MjIxNzAzcy0xLjA3NDIzMjczLS4wMzQ2MjI0OC0xLjk5MTg2ODkgMS4yNjg1ODY1MmMtLjI2MzU5ODc1LjU0Njk4ODQ1LS41NDY5NDE2NyAxLjExMDQ0NTk4LS4yMjg5NzYyNyAyLjIyMDg5MTk2LS40NTgwNDYxLS43NzYwMTE1LTIuNDMxNzYxNi00LjIxMjcxNDA5LTIuNDMxNzYxNi00LjIxMjcxNDA5czEuMzkyMTUxMzUtMi41MjA3NTA3NCA0Ljk1MjQxODc3LTIuNjYwNzg0NjV6IiBmaWxsPSIjZWYzZjM2Ii8+PHBhdGggZD0ibTEyLjE5NDI0Mzk1IDkuOTkzMjcwN3MtMS42MjYxMzM4NCAzLjEzMTkzMTE3LTUuNjI2MjkzOTUgMi45NzcwNjU3M2MuNDk0MjU5MzUtLjg1NTA4MTc3IDIuODQ2OTAzOS00LjkyOTM5OTUgMi44NDY5MDM5LTQuOTI5Mzk5NXMuNTY4NDE2OTYtLjkxMjcyMzUyLS4xMDIxMzYzMy0yLjM1OTI0MTUzYy0uMzQxMDc4MjUtLjUwMjQ5Mzg4LS42ODg3MDY3LTEuMDI4MDUzODItMS44MDg5Nzc5OC0xLjMwODE2ODQzLjkwMTIxMzktLjAwODE4Nzc1IDQuODYzNTIzMiAwIDQuODYzNTIzMiAwczEuNDg0MzY4OCAyLjQ2NjM4NDA4LS4xNzMwMTg4NCA1LjYxOTc0Mzc1eiIgZmlsbD0iI2ZjZDkwMCIvPjxwYXRoIGQ9Im0xLjgwMDAxMjkzIDEwLjAxNzk3NDMxcy0xLjg5OTYwNDY3LTIuOTczNzkwNjEuMjM1NTczMjUtNi4zNjEwODU5OGMuNDkyNjIxOC44NTUwODE3OCAyLjg0NTI2NjM0IDQuOTI5Mzk5NSAyLjg0NTI2NjM0IDQuOTI5Mzk5NXMuNTA3NDUzMzIuOTQ4OTgzNTYgMi4wOTQwMDUyNCAxLjA5MDYwODIzYy42MDQ2NzctLjA0NDQ0Nzc4IDEuMjM0MDEwODItLjA4MjM0NTM2IDIuMDM4MDQ3ODItLjkxMTAzOTE5LS40NDMyNjEzNy43ODQyNDYwNC0yLjQzMTg1NTE4IDQuMjExMDc2NTQtMi40MzE4NTUxOCA0LjIxMTA3NjU0cy0yLjg3OTg0MjA0LjA1MjcyOTEtNC43ODEwODQyNi0yLjk1ODk1OTF6IiBmaWxsPSIjNjFiYzViIi8+PHBhdGggZD0ibTYuNTY2MzEyNDUgMTIuOTk5OTk5NDcuODAwNjY4MzMtMy4zNDExNjMyNHMuODc5Nzg1MzgtLjA2OTI0NDk3IDEuNjE3ODk5My0uODc4MTQ3ODNjLS40NTgwNDYxLjgwNTY3NDU1LTIuNDE4NTY3NjMgNC4yMTkzMTEwNy0yLjQxODU2NzYzIDQuMjE5MzExMDd6IiBmaWxsPSIjNWFiMDU1Ii8+PHBhdGggZD0ibTQuMzAyNjEwMjYgNy4wMzc1ODY3MWMwLTEuNDcyODU5MTcgMS4xOTQ0NzU2OC0yLjY2NzMzNDg1IDIuNjY3MzM0ODUtMi42NjczMzQ4NXMyLjY2NzMzNDg1IDEuMTk0NDc1NjggMi42NjczMzQ4NSAyLjY2NzMzNDg0YzAgMS40NzI5MDU5NS0xLjE5NDQ3NTY4IDIuNjY3MzM0ODUtMi42NjczMzQ4NSAyLjY2NzMzNDg1LTEuNDcyODU5MTctLjAwMTYzNzU1LTIuNjY3MzM0ODUtMS4xOTQ0Mjg5LTIuNjY3MzM0ODUtMi42NjczMzQ4NXoiIGZpbGw9IiNmZmYiLz48cGF0aCBkPSJtODAuMDA0IDEyOS4wNTZjMC0yNi4xOTggMjEuMjM0LTQ3LjQ2NyA0Ny40NjgtNDcuNDY3IDI2LjE5OCAwIDQ3LjQ2NyAyMS4yMzQgNDcuNDY3IDQ3LjQ2NyAwIDI2LjE5OS0yMS4yMzMgNDcuNDY4LTQ3LjQ2NyA0Ny40NjgtMjYuMTk5IDAtNDcuNDY4LTIxLjI2OS00Ny40NjgtNDcuNDY4eiIgZmlsbD0idXJsKCNhKSIgdHJhbnNmb3JtPSJtYXRyaXgoLjA0Njc5IDAgMCAuMDQ2NzkgMS4wMDU4OTUgLjk5OTQyNikiLz48cGF0aCBkPSJtMTIuMzY1NTc4NDYgNC4zNzUyMTEzLTMuMjk2NzE1NDYuOTY3MDkwMThzLS40OTc1MzQ0NS0uNzI5ODc5MzgtMS41NjY3NjA5Ni0uOTY3MDkwMThjLjkyNzU1NTA1LS4wMDQ5NTk0NCA0Ljg2MzQ3NjQyIDAgNC44NjM0NzY0MiAweiIgZmlsbD0iI2VhY2EwNSIvPjxwYXRoIGQ9Im00LjM5OTgzMzk0IDcuNzUyNjM0NTdjLS40NjMwMDU1NC0uODAyMzUyNjYtMi4zNjc1MjI4Ni00LjA5MDc4NjgtMi4zNjc1MjI4Ni00LjA5MDc4NjhsMi40NDE2MzM2OSAyLjQxNTI0NTc0cy0uMjUwNDUxNTcuNTE1Njg3ODYtLjE1NjUwMjk5IDEuMjUzNzU1bC4wODIzNDUzNy40MjE3ODYwNnoiIGZpbGw9IiNkZjNhMzIiLz48L3N2Zz4=",
    "browser_img_alt": "Browser Logo",
    "browser_version": "Version 110.0.1.1.1122.112",
    "overall_status": "failstatus",
    "overall_status_text": "PASSED",
    "table_data": {
        "1": {
            "sno": 1,
            "rowspan": 3,
            "step": "Step 1",
            "expected_result": "Expected result 1",
            "actual_result": "Actual result 1",
            "overall_step_status": "Passed",
            "sub_steps": {
                "1": {
                    "sub_step": "open browser11",
                    "sub_step_message": "Additional information",
                    "image_src": "image1.png",
                    "image_alt": "Step Image",
                    "sub_step_status": "Pass"
                },
                "2":  {
                    "sub_step": "open browser12",
                    "sub_step_message": "Additional information",
                    "image_src": "image1.png",
                    "image_alt": "Step Image",
                    "sub_step_status": "Pass"
                }
            }
        },
        "2": {
            "sno": 2,
            "rowspan": 4,
            "step": "Step 1",
            "expected_result": "Expected result 1",
            "actual_result": "Actual result 1",
            "overall_step_status": "Passed",
            "sub_steps": {
                "1": {
                    "sub_step": "open browser",
                    "sub_step_message": "Additional information",
                    "image_src": "image1.png",
                    "image_alt": "Step Image",
                    "sub_step_status": "Pass"
                },
                "2":  {
                    "sub_step": "open browser",
                    "sub_step_message": "Additional information",
                    "image_src": "image1.png",
                    "image_alt": "Step Image",
                    "sub_step_status": "Pass"
                },
                "3":  {
                    "sub_step": "open browser",
                    "sub_step_message": "Additional information",
                    "image_src": "image1.png",
                    "image_alt": "Step Image",
                    "sub_step_status": "Pass"
                }
            }
        }
    }
}

def generate_html():
    # Setup Jinja2 environment and render the HTML template
    env = Environment(loader=FileSystemLoader("."))
    # Replace with the path to your template
    template = env.get_template("jinja2_template.html")
    output = template.render(data)
    print(output)

    # Save the populated HTML to a file
    with open("output.html", "w") as f:
        f.write(output)

    print("HTML file generated successfully!")
    return output
