print("🎉 Ура! Моя система настроена правильно!")
print(f"Текущая дата: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}")
print(f"Версия Python: {__import__('sys').version.split()[0]}")