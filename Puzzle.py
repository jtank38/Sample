import ConfigParser
import re





class PuzzleBall():

    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('C:\Users\Jubanjan\Desktop\Stuffs\Evaluation_Assignment\Balls_Puzzle\settings.cfg')
        self.FileInput = config.get('filename', 'File_Input')
        self.Balls_in_bags,self.Players_Number=self.ReadInputFile(self.FileInput)
        self.OutputList=self.Sort_List_Balls(self.Balls_in_bags,self.Players_Number)
        self.PrintOutPut(self.OutputList)

    def ReadInputFile(self,Filename):
        '''
        :param Filename:
        :return: Processed/Filtered ArrayInput and Processed/Filtered Test Cases
        '''
        with open(Filename) as f :
            content= f.read().split()
        Input= content[1].replace(","," ")
        Balls_Bags= [int(number) for number in re.findall(r'\d+', Input)]
        return Balls_Bags,int(content[2])

    def Sort_List_Balls(self,Balls_Bag,PlayerNumber):
        Balls_Bag.sort()
        Valid_list=[]
        for i in Balls_Bag:
            Valid_list.append(self.Valid_Numbers(Balls_Bag,i,PlayerNumber))

        LastNumber=min(Min for Min in Valid_list if Min != None)
        FirstNumber= Valid_list.index(LastNumber)
        return [i for i in Balls_Bag[FirstNumber:LastNumber]]


    def Valid_Numbers(self,Input_List,Number,PlayerNumber):

        Indx= Input_List.index(Number)+(PlayerNumber-1)
        Valid_Numbers=[i for i in Input_List[Indx:]]
        if len(Valid_Numbers)!=0 and Valid_Numbers[0]-Number>Number:
            return Valid_Numbers[0]-Number
        else:
            return None

    def PrintOutPut(self,Output):

        StrOutput=''
        for i in Output:
           StrOutput+= str(i)+','
        f=open("Output1.txt",'w+')
        f.write(StrOutput[:-1])
        f.close()
        print 'OutPut Complied!! Please Open Output.txt'



if __name__=='__main__':
    PuzzleBall()
