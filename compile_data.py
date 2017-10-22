import os

def compile_data():

        print('creating file...')
        
        f = open('data.csv', 'a')
        f.write('DateTime [UTC], TimeFromStart [s], Temperature [C], AbPressure [P], Altitude [m],\n')
        

        print('file created.')
        print('compiling data...')

        for filename in os.listdir('data'):
            print(filename)
            fr = open('data/' + str(filename), 'r')
            data_point = fr.read()
            f.write(data_point + '\n')

        print('data compiled.')
