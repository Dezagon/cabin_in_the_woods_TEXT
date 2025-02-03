import sys
import time
# import keyboard
from playsound import playsound

def delay_character(string: str):
    for c in string:
        if c == ".":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.4)
        elif c == "?":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.2)
        elif c == ",":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.5)
        elif c == "!":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.2)
        elif c == '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.5)
        elif c == " ":
            sys.stdout.write(c)
            sys.stdout.flush()
        else: 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)


def beginning() -> str:
    # !!!encase every desirable string in the character_delay() function!!!
    dialogue = [" \n",
                "\n...........it has been a long journey...too long in fact...looks like it's going to rain soon...I need to rest......\n",
                "????\n",
                "what is that???\n",
                "a cabin??\n",
                "all the way out here?\n",
                "....\n",
                "something's off, but I'm so tired...\n",
                "\ninvestigate the cabin | keep trudging\n"]
    
    for line in dialogue:
        delay_character(line)
        if line == " \n":
            playsound("sounds/thunder1.mp3")

    options = ["investigate the cabin", "keep trudging"]
    decision = input("")
    # counter for how many times the user does not input the one of two decisions available
    counter = 0

    # while loop checks the user's input and continues to ask for input if user did not type one of two responses
    while options.count(decision.lower()) != 1:
        delay_character("\nI need to make a decision...it's going to rain soon...\n")
        decision = input("")
        decision.lower()
        counter += 1

        # this while loop kicks in after asking for user input for the third time
        while counter >= 2 and options.count(decision.lower()) != 1:
            delay_character("ENOUGH DILLY DALLYING!!!, I NEED TO LOCK.IT.IN.\n")
            decision = input("")
            decision.lower()
            if counter == 4:
                dialogue = ["...I'm...cooked...\n",
                            " \n",
                            "You collapse on the ground after being unable to decide which path to go down\n",
                            "as you give in to your body's exhaustion, you lift your head weakly to see the very reason you felt something off in the first place...\n",
                            "perhaps you never had a chance from the start...\n",
                            "You were never seen again...\n"]
                
                for line in dialogue:
                    delay_character(line)
                    if line == " \n":
                        playsound("sounds/collapse.mp3")

                demise = "exhausted"
                return demise
            
            counter += 1

    return decision




def climax(decision: str) -> str:
    if decision.lower() == "keep trudging":
        dialogue = ["...yeah no thanks creepy cabin in the woods...\n",
                    "you continue past the cabin, looking back at its ominous state with contempt...\n",
                    "...ugh...\n",
                    "you can't deny that you are incredibly exhausted...you feel as though you're about to collapse\n",
                    " \n",
                    "!!!\n",
                    "you look around frantically, unable to locate the source of the sound\n",
                    "...\n",
                    "you spot it...\n"
                    "it is unlike anything you've ever seen...a horrifying anomaly...\n",
                    "as you are paralyzed from fear, the creature makes it's move, faster than you can blink...\n",
                    "  \n",
                    "...\n",
                    "you wake up feeling numb\n",
                    "huh...\n",
                    "as you stare up at the now raining sky, the creature walks into your field of view...except...it looks like....you...\n"]

        for line in dialogue:
            delay_character(line)
            if line == " \n":
                playsound("sounds/branch_snap.mp3")
            elif line == "  \n":
                playsound("sounds/bone_crack.mp3")

        demise = "impersonated"
        return demise

    if decision.lower() == "investigate the cabin":
        dialogue = ["...ugh it's better than getting caught in the rain...I guess...\n",
                    "you begrudgingly approach the cabin, the off putting feeling you had before only getting worse...\n",
                    "...you approach the door\n",
                    " \n",
                    "...\n",
                    "no answer...\n",
                    "you reach for the doorknob and push\n",
                    "  \n",
                    "!!!\n",
                    "it opened...\n",
                    "you are faced with two options...\n",
                    "walk in | walk away\n"]
        
        for line in dialogue:
            delay_character(line)
            if line == " \n":
                playsound("sounds/knock.mp3")
            elif line == "  \n":
                playsound("sounds/door_creak.mp3")
        
        decision = input("")
        decision.lower()
        options = ["walk in", "walk away"]
        counter = 0
        while options.count(decision.lower()) != 1:
            delay_character("c'mon now it's one or the other\n")
            decision = input("")
            decision.lower()
            if counter >= 2 and options.count(decision.lower()) != 1:
                dialogue = ["...\n",
                            "why am I so indecisive\n",
                            "the creature stalking you notices your incompetence and strikes\n",
                            "what a pathetic demise...\n"]
                for line in dialogue:
                    delay_character(line)
                
                demise = "indecisive"
                return demise
             
            counter += 1

        if decision.lower() == options[1]:
            dialogue = ["...yeah no thanks\n",
                        "you walk away from the ominous cabin, not wanting to deal with whatever bad juju it had\n",
                        " \n",
                        "!!!\n",
                        "  \n",
                        "you look back at the cabin and see a humanoid creature heading straight to you at an alarming rate\n",
                        "you run but the creature is faster...\n",
                        "it's over...\n",
                        "   \n",
                        "a permanent look of horror is strewn across your face as the creature drags your lifeless corpse back to the cabin...\n"]
            
            for line in dialogue:
                delay_character(line)
                if line == " \n":
                    playsound("sounds/scream.mp3")
                elif line == "  \n":
                    playsound("sounds/running.mp3")
                elif line == "   \n":
                    playsound("sounds/bone_crack.mp3")
            
            demise = "outran"
            return demise


        if decision.lower() == options[0]:
            dialogue = ["...\n",
                        "as your eyes adjust to the darkness and you see what you would normally expect from a cabin\n",
                        "...a table\n",
                        "...chairs\n",
                        "...a kitchen\n",
                        "...and a single knife embedded on the wooden countertop\n",
                        "you feel a slight sense of...welcome?...comfort?...\n",
                        "rain begins to pour\n",
                        "at least I'm not out there...hmmm...\n",
                        "this feeling of comfort...is...incredibly...soothing\n",
                        "...\n",
                        " \n",
                        "!!!\n",
                        "you scour the cabin windows in search of the source of the noise...\n",
                        "then...\n",
                        "you see it...and it sees you...it smiles...\n",
                        "  \n",
                        "...it broke in...\n",
                        "just as it begins to lunge, you instinctively grab the knife\n",
                        "you get in a defensive stance as the creature stares at you...waiting for an opening...still smiling...\n",
                        "fight | submit\n"]
            
            for line in dialogue:
                delay_character(line)
                if line == " \n":
                    playsound("sounds/hello.mp3")
                elif line == "  \n":
                    playsound("sounds/glass_shattering.mp3")
            
            options = ["fight", "submit"]
            decision = input("")
            while options.count(decision.lower()) != 1:
                decision = input("fight | submit")
                
            if decision.lower() == options[0]:
                dialogue = ["you lunge at the creature\n",
                            " \n",
                            "your unpredictability startles it....and you are able to kill it\n",
                            "you are relieved....no....satisfied.......euphoric.....\n",
                            "you stare at the creature's lifeless body....and smile...\n"]

                for line in dialogue:
                    delay_character(line)
                    if line == " \n":
                        playsound("sounds/stab.mp3")

                demise = "turned"
                return demise

            if decision.lower() == options[1]:
                dialogue = ["you feel an overwhelming sense of....defeat?...wash over you....\n",
                            "you attempt to fight it but it is simply too strong...\n",
                            "you fall to your knees and drop the knife...\n",
                            "the creature finds great pleasure in your defeat...as you...become its next victim...\n"]

                for line in dialogue:
                    delay_character(line)

                demise = "defeat"
                return demise



                

        
                    
def main():
    endings = ["exhausted", "impersonated", "indecisive", "outran", "turned", "defeat"]
    running = True
    while running:
        beginning_outcome = beginning() 
        if beginning_outcome == "exhausted":
            running = False
        climax_outcome = climax(beginning_outcome)
        for ending in endings:
            if climax_outcome == ending:
                running = False
        

    exit()



    










if __name__ == "__main__":
    main()
