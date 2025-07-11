EXTREMELY basic workout app skeleton: Basically just what I wish was in my ideal workout app.

--- USER FLOW ---

OPEN -> [New exercise/Load from file]
WHILE TRUE: Q TO CANCEL (+ confirmation)

[New Exercise]
- Exercise name
- Menu (add, remove, edit, etc.)

[Load from file]
- Enter name:
- search
- found/notfound (if not found, repeat)

[BEGIN WORKOUT]
- Start stopwatch (thread) -> Stopwatch on top
- List exercises -> Next / Select (from incomplete) / Finish Workout

[CURRENT EXERCISE]
- CURRENT SET: next (Start new timer), skip, edit (weight/reps)
- ADD SET


CHECKLIST
- Timer [✓]
- New workout (file reading/editing) [✓]
  - Name, sets, reps, weights/prev, ~~type (bodyweight, dumbbell, machine, barbell)~~ [✓]
- Menu
- Superset
- Dumbbell/Barbell/Machine selection
- Alternative exercise selection
- Warmup Set
- Add comment/add video
- calculate workout time from start to final exercise


IDEAS
- During a set/exercise, pop out a new terminal with functioning stopwatch/timers

TODO:
- Figure out threads
- argument to open a specific exercise .json file