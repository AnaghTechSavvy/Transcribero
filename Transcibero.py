from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
name=input("enter your username:  ")
name_conform=input("re-enter your username: ")
if name==name_conform: 
    print("\n======Welcome to Transcribero=====")
    dna_list=[]
    while True:
        user_input=input("enter few actual DNA sequences (type DONE if finished):").upper().strip()
        if user_input=="DONE":  
            print(f" sequence locked in by user id : {name}")
            break
        dna_list.append(Seq(user_input))
for s in dna_list:
    print(f"The transcribed mRNA strands are: {s.transcribe()}")
print(f"Thank you for using ANAGH'S Transcribero dear {name}")
input("\nProcessing complete! Press ENTER to exit the program...")

            
