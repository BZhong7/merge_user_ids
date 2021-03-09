import merge_user_ids


list1 = [{"helpdesk_id": 1, "name": "will", "phone_number": "p1", "color": "green"},
         {"helpdesk_id": 2, "name": "bill", "email": "pasta.com"}]

list2 = [{"helpdesk_id": 1, "city": "nyc"},
         {"email": "pasta.com", "pet": "dog", "phone_number": "p1"},
         {"city": "queens", "cheese": "stinky"},
         {"helpdesk_id": 1, "color": "red"}]

list3 = []

merged_list = merge_user_ids.merge_user_ids(list1, list2)

for j in merged_list:
    print(j)
