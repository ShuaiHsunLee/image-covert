# when add new png, run update
update:
	@find "png" -type f > updatelist
	@echo "%" >> updatelist
	@find "txt" -type f >> updatelist
	@echo "%" >> updatelist
	@cd src && python3 update.py && python3 png_to_txt.py

# when pattern define change, run updateall
updateall:
	@rm -f txt/*
	@find "png" -type f > updatelist
	@echo "%" >> updatelist
	@find "txt" -type f >> updatelist
	@echo "%" >> updatelist
	@cd src && python3 update.py && python3 png_to_txt.py