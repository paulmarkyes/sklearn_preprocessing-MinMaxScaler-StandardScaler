#coding=gbk
from sklearn.preprocessing import MinMaxScaler, StandardScaler
'''���ݵ���������'''
def minMax():
    '''
    ���ݵĹ�һ��������ĳһ���������ս����ɺܴ��Ӱ��
    ȱ�㣺�������쳣���Ӱ��
    '''
    mms = MinMaxScaler()
    data = mms.fit_transform([[90, 2, 10, 40],
                              [60, 4, 15, 45],
                              [75, 3, 13, 46]])
    print(data)
def standar():
    '''
    ���ݵı�׼��������쳣��Խ��Ӱ��ܴ�����⣬������ά�ֺܺõ��ȶ���
    '''
    stand =  StandardScaler()
    data =  stand.fit_transform([[1, -1, 3], [2, 4, 2], [4, 6, -1]])
    print(data)
def main():
    #minMax()
    standar()
if __name__ == "__main__":
    main()