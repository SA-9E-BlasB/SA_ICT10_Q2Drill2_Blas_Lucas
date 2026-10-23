from pyscript import document

# these are the starting members for each grade. sets only keep unique names
grade_7 = {"Alice Blue", "Anita Bath", "Billy Sparks", "Eileen Dover"}
grade_8 = {"Ella Vator", "Francisco Portero", "Joe Kerr", "Juanito Lakarin"}
grade_9 = {"Justin Case", "Ligaya Anonuevo", "Paige Turner", "Restituto Fruto"}
grade_10 = {"Sheldon Cooper", "Tam Nguyen"}

# starts as an empty set so new names can be added later
new_members = set()


def show_members():
    # the | symbol joins all five sets into one, so repeated names only show once
    all_members = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # sorted puts the names in abc order so the roster is easier to read
    # lambda tells map how to turn each name into an html list item
    # map does that for every name, then join connects the items into one html string
    member_rows = "".join(
        map(lambda name: f"<li>{name}</li>", sorted(all_members))
    )

    # this f-string puts the member count and list into the output box
    # :02d shows the total with at least two digits, like 07 instead of 7
    document.getElementById("output").innerHTML = f"""
        <div class="total-box">
            <div>
                <span>REGISTERED MEMBERS</span>
                <p>Unique names across all grade levels</p>
            </div>
            <strong>{len(all_members):02d}</strong>
        </div>
        <div class="list-heading">MEMBER ROSTER <span>A–Z</span></div>
        <ul class="member-list">{member_rows}</ul>
    """


def result_checker(event):
    # gets what was typed in both boxes. strip removes spaces at the ends
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    # the f-string combines both names with a space between them
    full_name = f"{first_name} {last_name}".strip()

    # this uses set difference (-) to avoid adding incomplete names
    # when a box is empty, the full name matches one of the names being removed
    # update then adds the name only when both boxes have something typed
    valid_members = {full_name} - {"", first_name, last_name}
    new_members.update(valid_members)

    # empties both boxes after submit, then shows the updated roster
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
    show_members()


# runs once when the page loads so the starting roster appears right away
show_members()
