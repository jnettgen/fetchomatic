import json

def main():
	for unit in data['definitions']:
		print("\n" + '-'*35)
		print(f"Target: {unit['name']}")
		print(f"id:   {unit['id']}")
		for childTarget in unit['childTargets']:
			print(f"        name:  {childTarget['name']}")
			print(f"        definitionId:  {childTarget['definitionId']}")
			print(f"        id:  {childTarget['id']}\n")
			try:
				for sub in childTarget['childTargets']:
					print(f" 			name:  {sub['name']}")
					print(f" 			parentId:  {sub['parentId']}")
					print(f" 			definitionId: {sub['definitionId']}")
					print(f" 			id: {sub['id']}\n")
			except:
				continue
			try:
				for sub2 in sub['childTargets']:
					print(f" 				name:  {sub2['name']}")
					print(f" 				parentId:  {sub2['parentId']}")
					print(f" 				definitionId: {sub2['definitionId']}")
					print(f" 				id: {sub2['id']}\n")
			except:
				continue
			try:
				for sub3 in sub2['childTargets']:
					print(f" 					name:  {sub3['name']}")
					print(f" 					parentId:  {sub3['parentId']}")
					print(f" 					definitionId: {sub3['definitionId']}")
					print(f" 					id: {sub3['id']}\n")
			except:
				continue

if __name__ == '__main__':
	main()