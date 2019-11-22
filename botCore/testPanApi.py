from baidupcsapi import PCS
pcs=PCS('17624071108','')
print(pcs.quota().content)
print(pcs.list_files('/').content)