
"""
Dictionaries
"""

import speech_recognition as speech
import pyttsx3
import pygame

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',200)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('CatEXA')

#Display the Background Image
bg=pygame.image.load("images/bg1.jpg").convert_alpha()
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

engine.runAndWait()
engine.say("Hello!! I am your assistent for cats. You can ask me queries related to Cats !")
engine.runAndWait()

places={
        "how many": ["spch","There are 38 species of cats"],
        "scottish": ["spch","Scottish fold cats are known to possess an easy-going nature, and to be very loving and friendly with people and other household pets. This breed, outgoing and playful, tends to become particularly attached to one family member. The Scottish fold cat is also known for its soft voice and the ability to speak in a variety of different-sounding purrs and meows not commonly heard in many other cat breeds."],
        "sphynx": ["spch","The Sphynx, a hairless, wrinkled wonder with big ears and eyes and pronounced cheekbones is one of the newer cat breeds. The first Sphynx was born in Canada in 1966, according to the CFA. The lack of hair, a genetic anomaly, was a result of Mother Nature and occurs about once every 15 years. Since this time, the Sphynx has been bred with traditional shorthair cats, and then bred back to hairless to create a genetically sound, healthy breed. "],
        "devon": ["spch","The Devon Rex is a relatively newer breed of cats, discovered by accident in the region of Devonshire, England, in 1960 and has been called many things: a pixie cat, an alien cat, a cat that looks like an elf — or a bat. It is also known to behave more like a dog than like a cat. With its unique appearance, the breed has captured the attention of cat lovers worldwide—and the hearts of its families with its lovable, quirky and mischievous personality"],
        "american": ["spch","The American shorthair cat has a reputation as “America’s breed”. The first cats of this type were brought over from Europe with early settlers. Today, the American shorthair is a family favorite. It consistently ranks as one of the 10 most popular cat breeds. The breed is known to have a very even temperament with a good disposition and keen intelligence. Another testament to its mellow nature is the shorthair’s ability to get along with other pets and its gentle nature around children. A shorthair is considered an ideal pet for a working family with children."],      
        "Maine coon":["spch","Maine coon cat -  Maine coon is one of the oldest natural breeds in North America, Maine Coon cats are known for their intelligence and playfulness, as well as their size. One of the largest breeds of domestic cats, they are lovingly referred to as “gentle giants.” Maine Coons are also known for their shaggy coats and rugged appearance. Full-grown male Maine Coons can grow to be 30 lbs., with females weighing a little less. These gentle giants generally reach full size by age three to five. Maine Coons are people-oriented, energetic and highly-intelligent, making them an easy breed to train. They’re also known for their dog-like behavior: following their owners from room to room, coming when called and playing fetch with their owners"], 
        "British":["spch","British shorthair - It is believed that the Romans brought the British shorthair to England during the first century, at which time the breed co-existed and bred with wild cats native to England. Many years later, the British shorthair was crossbred with Persian cats, slightly changing the look of the cat and improving the thickness of its fur coat.Not only is it one of the most popular cat breeds, it is also commonly selected to appear on TV, in movies and even in books. You might recognize the cat in many Whiskas brand ads as a British shorthair. The cat raised from the dead in Stephen King’s Pet Sematary (“Winston Churchill”) was a British shorthair, as was “Arlene” in Garfield: The Movie and the “Cheshire Cat” in Alice’s Adventures in Wonderland, just to name a few"],
        "Persian":["spch","Known for their gentle, laid-back personalities, sweet faces and round eyes, Persian cats are affectionate, quiet, beautiful creatures of habit, making them the most popular breed among cat fanciers. Persian cats are not only the most popular breed of cats, they’ve also been around the longest. In fact, hieroglyphics reference their origination as far back a 1684 B.C. Thought to have originated in Persia (now Iran), the cats were named after their believed “country of origin.” Although the breed has evolved over time in color and body type, one thing has remained the same: its thick and full fur. Ideally, Persians should be groomed at least once a day to prevent knots and matting of the fur. Persians should also be bathed occasionally to maintain a clean and healthy coat."],
        "Exotic":["spch","For the third year in a row, the Exotic cat has been named as America's most popular registered cat, knocking the Persian off the podium again after 31 years as the reigning No. 1 breed. The Exotic (also called the Exotic shorthair by some cat associations) is a cross between Persians and American Shorthairs. Exotic cats are bred to meet the Persian standard in almost every way with one exception: their coats. Exotics, unlike their Persian counterparts, have short, thick, dense coats, making them popular among people who enjoy the Persian personality but don’t want the hassle or the time required for daily grooming. The Exotic personality tends to mimic that of a Persian: sweet, affectionate and playful. Exotic cats are known to show more affection and loyalty than other feline breeds, and commonly follow their owners throughout the home."],
        "cats live":["spch","Cats live about 2 to 16 years."],
        "chew":["spch","Sometimes cats chew the home plants because they may be in need of more fiber in their diet. Substitute those lush leaves (which may be topped with toxic pesticides) for small portions of baked or steamed vegetables such as carrots, broccoli, asparagus, or squash"],
        "whiskers":["spch","Whiskers are specifically tuned sensory equipment that guide a cat through daily functions. These specialized hairs aid vision and help a kitty navigate his environment, providing additional sensory input, much like antennae on insects"],
        "biggest":["spch","Tiger is worlds biggest cat"]   
        }
answer="No"
activate="none"
exitstatus="no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 'c' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("c pressed")
                    
                    
        #If 'c' key is pressed
        if activate=='c':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg.jpg").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in places:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                               # image=pygame.image.load("images/"+places[keyword][0]+".jpg").convert_alpha()
                               # image1=pygame.transform.scale(image, (900,600))
                               # screen.blit(image1,(0,0))
                               # pygame.display.update()
                               
                               engine.runAndWait()
                               engine.say(places[keyword][1])
                               engine.runAndWait()
       
        
           
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/bg1.jpg").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                
