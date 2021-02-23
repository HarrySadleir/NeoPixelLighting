# The main file for this project. 
# USAGE
import sys
import effects

def loop_rc():
    while True:
        if len(sys.argv) == 4:
            effects.rainbow_cycle(float(sys.argv[2]), int(sys.argv[3]))
        else:
            effects.rainbow_cycle()
        

def main():
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '-cleanup':
                effects.cleanup()
                exit()
            
            if sys.argv[1] == '-solid':
                if len(sys.argv) != 5: 
                    print("USAGE: main.py -solid r g b")
                    exit()
                effects.solid(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
            
            if sys.argv[1] == '-loop_rc':
                loop_rc()
                
        else:
            loop_rc()
    except:
        pass
    finally:
        effects.cleanup()

if __name__ == "__main__":
    main()

    
    