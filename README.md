Python version: 3.10.4
assets found on Itch.io

| Player | Movement   | Attack | Defend |
| ------ | ---------- | ------ | ------ |
| 1      | WASD       | Q      | E      |
| 2      | Arrow Keys | {      | }      |

## More or less what I wanted the game to run like

```mermaid
stateDiagram
direction LR
	[*] --> Home
	Home --> character_selection
	character_selection --> game

	game --> Pause
	game --> end_screen

	end_screen --> character_selection
	end_screen --> Home

	Pause --> character_selection
	Pause --> Home

	state game {
		direction LR
		check_health : player health at 0?

		[*] --> take_input
		take_input --> check_for_collison
		check_for_collison --> update_character
		update_character --> check_health
		check_health --> [*] : YES
		check_health --> take_input : NO
	}

```

## what i wanted the event loop to look like

```mermaid

stateDiagram
direction LR

	[*] --> isRunning
	isRunning --> [*] : False
	isRunning --> Game_loop : True
	Game_loop --> isRunning

	state Game_loop{
		[*] --> get_dt
		get_dt --> event_loop
		get_dt --> update_loop
		get_dt --> render_loop

		event_loop --> [*]
		update_loop --> [*]
		render_loop --> [*]

		state event_loop{
			[*] --> pass_event_to_objs
			pass_event_to_objs --> [*]
		}

		state update_loop{
			[*] --> update_objs
			update_objs --> [*]
		}

		state render_loop{
			[*] --> render
			render --> render_background
			render_background --> render_game_obj
			render_game_obj --> render_ui
			render_ui --> [*]
		}
	}



```
