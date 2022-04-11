# dictionary
# di dictionary ada 2 items yaitu {keys, values}
member = {"Id": 212,
          "Nama": "Hefry Anesti",
          "Pekerjaan": "Siswa",
          "Member": "Silver"
          }
print(member)
print(member["Id"]) # cara memanggil keys
print(member.keys()) # mengetahui keys
print(member.values()) # mengetahui values
print(member.items()) # mengetahui item

print(100*'=')

member2 = {'Id': 213,
           'Nama': 'Niba',
           'Pekerjaan': 'Siswa',
           'Member': 'gold'
           }
print(member2)

print(100*'=')

# can also call with like this
memberlist = {212:member,213:member2}
print(memberlist[212]) # antara call dictionary first data or second data