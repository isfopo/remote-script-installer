install:
	npm run build && python3 scripts/install.py --name RemoteScriptInstaller

watch:
	python3 scripts/watch.py --version 'Live 12.0.15'

close-set:
	pkill -x Ableton Live 11 Suite

open-set:
	open set/oscdevset.als

reload:
	just install && just close-set && sleep 1 && just open-set

rename:
	python3 scripts/rename.py