# Brandon Zhong - Merge User IDs


# Main function that calls all other functions in order to merge the two lists together

# If there are no objects in existing_users, just merge new user objects within the list
# Otherwise merge the lists together, then merge objects together within the new list if needed
def merge_user_ids(existing_users, new_users):
    if len(existing_users) == 0:
        return merge_single_list(new_users)
    else:
        final_list = merge_two_lists(existing_users, new_users)
        return merge_single_list(final_list)


# Merge objects together within the same list using nested loop
# When objects have been "merged", discard the "used" object

# Make sure to avoid merging two identical objects, since they're sharing the same list
def merge_single_list(users):
    for i in users:
        for k in users:
            if i != k:
                has_merged = merge_objects(i, k)
                if has_merged:
                    users.remove(k)

    return users


# Merge list of existing users with list of new users

# First check to see if any existing objects can be merged with new objects
# When objects have been "merged", discard the "used" object
# Then append the rest of the unmerged objects on to the merged list
def merge_two_lists(existing_list, new_list):
    for x in existing_list:
        for i in new_list:
            has_merged = merge_objects(x, i)
            if has_merged:
                new_list.remove(i)

    for k in new_list:
        existing_list.append(k)

    return existing_list


# Merges two objects if it fulfills the necessary conditions
# Returns True or False if merging was successful or not
def merge_objects(obj1, obj2):
    if "helpdesk_id" in obj1 and "helpdesk_id" in obj2:
        if obj1["helpdesk_id"] == obj2["helpdesk_id"]:
            obj1.update(obj2)
            return True

    if "email" in obj1 and "email" in obj2:
        if obj1["email"] == obj2["email"]:
            obj1.update(obj2)
            return True

    if "phone_number" in obj1 and "phone_number" in obj2:
        if obj1["phone_number"] == obj2["phone_number"]:
            obj1.update(obj2)
            return True

    return False
