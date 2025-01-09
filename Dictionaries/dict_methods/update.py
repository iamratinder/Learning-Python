# update() : updates the value of key provided to it if the item already exists in dict,
#            else it creates a new key-value pair.
info = {"name": "Ratinder", "age": 18, "eligible": True}
print(info)                              ;print('─'*70)
info.update({"age": 18.5})
info.update({"DOB": 2005})
print(info)                              ;print('─'*70)

info_extra = {24: "employee1", 25: "employee2"}
info.update(info_extra)
print(info)                              ;print('─'*70)

