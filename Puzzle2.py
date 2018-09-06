import ConfigParser
import collections
import re
import operator


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
        '''

        :param Balls_Bag:
        :param PlayerNumber:
        :return: List of Desired Bags of Balls
        '''

        Balls_Bag.sort()   #TimSort O (nlogn)
        Eligible_FirstNumbers=collections.deque()
        for indx,Bags in enumerate(Balls_Bag[0:(len(Balls_Bag)-PlayerNumber)+1]):  #Slicing to Get to valid set of bags of balls possible
            Eligible_FirstNumbers.append(indx)
        Result_Inx=[]
        while (Eligible_FirstNumbers):
            Ind=Eligible_FirstNumbers.pop()
            if Balls_Bag[Ind+(PlayerNumber-1)]-Balls_Bag[Ind] > Balls_Bag[Ind]:
                Result_Inx.append((Ind,Balls_Bag[Ind+(PlayerNumber-1)]-Balls_Bag[Ind]))
            else:
                print 'false'
        FirstIndex= min(Result_Inx, key=operator.itemgetter(1))[0]
        return [i for i in Balls_Bag[FirstIndex:FirstIndex+PlayerNumber]]

    def PrintOutPut(self,Output):
        '''

        :param Output_List
        :writes to file output.txt the desired output
        '''

        StrOutput=''
        for i in Output:
           StrOutput+= str(i)+','
        f=open("Output1.txt",'w+')
        f.write(StrOutput[:-1])
        f.close()
        print 'OutPut Complied!! Please Open Output.txt'



if __name__=='__main__':
    PuzzleBall()
