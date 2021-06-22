from time import sleep
import pyautogui as pag
from playsound import playsound

pag.PAUSE = 0.5

folder = 'imdata/'
commands = ['quit', 'rawconv', 'offset', 'dark', 'flat', 'preproc', 'conv', 'stel_reg', 'sequence', 'crop', 'rgb_sep']
batches = []

auto = input('Would you like for the image processing to be automatic? (y/n) ')
if auto == 'y':
    series = int(input('How many image batches would you like to process? '))
    for i in range(0, series):
        obj_name = input('Starting name for object images: ')
        batches.append(obj_name)
        master = input('Are master frames already made? (y/n)')


def wait():
    sleep(2)
    while pag.locateCenterOnScreen(folder + 'busy2.png'):
        sleep(1)


def crop():
    x1 = '266'
    y1 = '4019'
    x2 = '6288'
    y2 = '1'
    print('Please switch to IRIS window.')
    sleep(5)

    pag.click(folder + 'geometry.png')
    pag.click(folder + 'crop.png')

    pag.moveTo(folder + 'x1.png')
    pag.moveRel(30, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(x1)

    pag.moveTo(folder + 'x2.png')
    pag.moveRel(30, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(x2)

    pag.moveTo(folder + 'y1.png')
    pag.moveRel(30, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(y1)

    pag.moveTo(folder + 'y2.png')
    pag.moveRel(30, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(y2)

    pag.click(folder + 'ok.png')


def digital_photo():
    print('Please switch to IRIS window.')
    sleep(5)

    pag.moveTo(folder + 'digitalphoto.png', duration=0.5)
    pag.click()


def rawconv():
    digital_photo()
    pag.moveTo(folder + 'decoderaw.png', duration=0.75)
    pag.click()

    sleep(1)
    playsound(r"D:\Dokumenti\INFORMATIKA\PYTHON\sound.mp3")
    print('Please drag and drop needed images (and calibration frames) in the dialog box.')
    zone = input('Crop image? (y/n) ')
    x1 = '265'
    y1 = '4020'
    x2 = '6288'
    y2 = '1'
    go = input('Press ENTER to continue... ')
    if go == '':
        print('Please switch to IRIS window.')
        sleep(5)
    if zone == 'y':
        try:
            pag.click(folder + 'zone.png')
            pag.moveTo(folder + 'x_1.png')
            pag.moveRel(40, 0)
            pag.doubleClick()
            pag.typewrite(x1)

            pag.moveTo(folder + 'y_1.png')
            pag.moveRel(40, 0)
            pag.doubleClick()
            pag.typewrite(y1)

            pag.moveTo(folder + 'x_2.png')
            pag.moveRel(40, 0)
            pag.doubleClick()
            pag.typewrite(x2)

            pag.moveTo(folder + 'y_2.png')
            pag.moveRel(40, 0)
            pag.doubleClick()
            pag.typewrite(y2)
        except Exception:
            pass

    pag.moveTo(folder + 'name.png', duration=0.25)
    pag.moveRel(50, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(obj_name)
    pag.click(folder + 'cfa.png')
    wait()
    '''
    repeat = input('Would you like to repeat the process? (y/n) ')
    pag.click(folder + 'done.png')
    if repeat:
        rawconv()
    '''


def offset():
    gen_name = 'bias'
    num = input('Number of bias frames: ')

    digital_photo()
    pag.click(folder + 'offset.png')
    pag.typewrite(gen_name)

    pag.moveTo(folder + 'number.png', duration=0.5)
    pag.moveRel(70, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(num)

    pag.click(folder + 'ok.png')
    wait()

    pag.click(folder + 'cmd.png')
    pag.press('enter')
    pag.typewrite('SAVE master-bias')
    pag.press('enter')
    pag.click(folder + 'exit.png')


def dark():
    gen_name = 'dark'
    offset_im = 'master-bias'
    number = input('Number of dark frames: ')

    digital_photo()
    pag.moveTo(folder + 'dark.png', duration=0.75)
    pag.click()

    pag.moveTo(folder + "gen_name.png", duration=0.5)
    pag.moveRel(115, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(gen_name)

    pag.moveTo(folder + "offset_im.png", duration=0.5)
    pag.moveRel(120, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(offset_im)

    pag.moveTo(folder + "number.png", duration=0.5)
    pag.moveRel(85, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(number)
    pag.moveTo(folder + "ok.png", duration=0.5)
    pag.click()
    wait()

    pag.click(folder + 'cmd.png')
    pag.press('enter')
    pag.typewrite('SAVE master-dark')
    pag.press('enter')
    pag.click(folder + 'exit.png')


def flat():
    gen_name = 'flat'
    offset_im = 'master-bias'
    norm_val = input('Normalization value (1000): ')
    number = input('Number of flat frames: ')

    digital_photo()
    pag.moveTo(folder + 'flat_field.png', duration=0.75)
    pag.click()

    pag.moveTo(folder + "gen_name.png", duration=0.5)
    pag.moveRel(125, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(gen_name)

    pag.moveTo(folder + "offset_im.png", duration=0.5)
    pag.moveRel(130, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(offset_im)

    pag.moveTo(folder + "norm_val.png", duration=0.5)
    pag.moveRel(105, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(norm_val)

    pag.moveTo(folder + "number.png", duration=0.5)
    pag.moveRel(100, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(number)
    pag.moveTo(folder + "ok.png", duration=0.5)
    pag.click()
    wait()

    pag.click(folder + 'cmd.png')
    pag.press('enter')
    pag.typewrite('grey_flat')
    pag.press('enter')

    pag.press('enter')
    pag.typewrite('SAVE master-flat')
    pag.press('enter')
    pag.click(folder + 'exit.png')


def preproc():
    cosme_query = input('Is there a cosmetic file in the working directory? (y/n)')
    if cosme_query == 'y':
        cosme = input('Cosmetic file name: ')
        number = input('Number of image files: ')

        in_gen_name = obj_name
        offset_im = 'master-bias'
        dark_im = 'master-dark'
        flat_field = 'master-flat'
        out_gen_name = obj_name + '-cal'

        digital_photo()
        pag.moveTo(folder + 'preprocessing.png', duration=0.75)
        pag.click()
        '''
        try:
            pag.moveTo(folder + 'tickbox.png', duration=0.5)
            pag.click()
        except:
            pass
        '''
        pag.moveTo(folder + 'input_gen_name.png', duration=0.5)
        pag.moveRel(135, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(in_gen_name)

        pag.moveTo(folder + 'offset_im.png', duration=0.5)
        pag.moveRel(165, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(offset_im)

        pag.moveTo(folder + 'input_dark.png', duration=0.5)
        pag.moveRel(165, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(dark_im)

        pag.moveTo(folder + 'input_flat_field.png', duration=0.5)
        pag.moveRel(160, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(flat_field)

        pag.moveTo(folder + 'cosme_file.png', duration=0.5)
        pag.moveRel(200, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(cosme)

        pag.moveTo(folder + 'output_gen_name.png', duration=0.5)
        pag.moveRel(135, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(out_gen_name)

        pag.moveTo(folder + 'number.png', duration=0.5)
        pag.moveRel(115, 0, duration=0.5)
        pag.doubleClick()
        pag.typewrite(number)

        pag.click(folder + "ok.png")
        wait()
    else:
        preproc()


def conv():
    gen_in_name = obj_name + '-cal'
    gen_out_name = gen_in_name + '-conv'
    num = input('Number of star images: ')
    digital_photo()
    pag.moveTo(folder + 'conv.png', duration=0.5)
    pag.click()

    pag.moveTo(folder + 'gen_in_name.png', duration=0.5)
    pag.moveRel(135, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(gen_in_name)

    pag.moveTo(folder + 'gen_out_name.png', duration=0.5)
    pag.moveRel(135, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(gen_out_name)

    pag.moveTo(folder + 'conv_number.png', duration=0.5)
    pag.moveRel(115, 0, duration=0.5)
    pag.doubleClick()
    pag.typewrite(num)

    pag.click(folder + "ok.png")
    wait()


def stel_reg():
    in_gen_name = obj_name + '-cal-conv'
    out_gen_name = obj_name + '-reg'
    num = input('Number of images: ')
    print('Please switch to IRIS window.')
    sleep(5)
    pag.click(folder + 'processing.png')
    pag.click(folder + 'stel_reg.png')

    pag.moveTo(folder + 'stel_in_gen_name.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(in_gen_name)

    pag.moveTo(folder + 'stel_out_gen_name.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(out_gen_name)

    pag.moveTo(folder + 'stel_num.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(num)
    try:
        pag.click(folder + 'glob_match.png')
    except Exception:
        pass
    try:
        pag.click(folder + 'quadratic.png')
    except Exception:
        pass
    pag.click(folder + 'ok.png')
    wait()


def sequence():
    in_gen_im = obj_name + '-reg'
    num = input('Number of images: ')
    print('Please switch to IRIS window.')
    sleep(5)
    pag.click(folder + 'processing.png')
    pag.click(folder + 'sequence.png')

    pag.moveTo(folder + 'seq_input.png')
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(in_gen_im)

    pag.moveTo(folder + 'seq_num.png')
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(num)

    pag.click(folder + 'ok.png')
    wait()
    pag.click(folder + 'cmd.png')
    pag.press('enter')
    stacked = obj_name + '-stk'
    pag.typewrite(f'SAVE {stacked}')
    pag.press('enter')
    pag.click(folder + 'exit.png')


def rgb_sep():
    red = obj_name + '-final-r'
    green = obj_name + '-final-g'
    blue = obj_name + '-final-b'
    digital_photo()
    pag.click(folder + 'rgb_sep.png')

    pag.moveTo(folder + 'red.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(red)

    pag.moveTo(folder + 'green.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(green)

    pag.moveTo(folder + 'blue.png', duration=0.25)
    pag.moveRel(100, 0, duration=0.25)
    pag.doubleClick()
    pag.typewrite(blue)

    pag.click(folder + 'ok.png')
    wait()


print('List of commands: ')
print('quit       -    shuts down the program \nrawconv    -    converts raw files to CFA files'
      '\noffset     -    creates master bias \ndark       -    cretes master dark'
      '\nflat       -    creates master flat \npreproc    -    applies calibration frames to object images'
      '\nconv       -    converts CFA files to RGB \nstel_reg   -    aligns images based on stars'
      '\nsequence   -    stacks images \ncrop       -    crops extra part of the image'
      '\nrgb_sep    -    separates image to individual RGB layers')

if auto == 'n':
    run = True
    while run:
        x = input('\nInput desired operation: ')
        if x in commands:
            if x != 'quit':
                print('Executing command...\n')
            if x == 'rawconv':
                rawconv()
            if x == 'offset':
                offset()
            if x == 'dark':
                dark()
            if x == 'flat':
                flat()
            if x == 'preproc':
                preproc()
            if x == 'conv':
                conv()
            if x == 'stel_reg':
                stel_reg()
            if x == 'sequence':
                sequence()
            if x == 'crop':
                crop()
            if x == 'rgb_sep':
                rgb_sep()
            if x == 'quit':
                run = False
                print('Program will shut down.')
            playsound(r"D:\Dokumenti\INFORMATIKA\PYTHON\sound.mp3")
        else:
            print('Unknown command.')

elif auto == 'y':
    for image in batches:
        obj_name = image
        rawconv()
        if master == 'n':
            offset()
            dark()
            flat()
        preproc()
        conv()
        stel_reg()
        sequence()
        rgb_sep()
        print(f'{obj_name} batch has sucessfully finished processing!')
    playsound(r"D:\Dokumenti\INFORMATIKA\PYTHON\sound.mp3")
    print('Program has sucessfully finished! Please check the IRIS working directory.')
