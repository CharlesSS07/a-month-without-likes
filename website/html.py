
import metadata

def centered_horizontally(a):
    '''This function should result in the content looking centered horizontally.'''
    return a.div(style=f'margin:0 auto;')

def centered_horizontally(a, width, units='px'):
    '''This function should result in the content looking centered horizontally.'''
    return a.div(style=f'width:{width}{units}; margin:0 auto;')

def centered_vertically(a, height, units='px'):
    return a.div(style=f'height:{height}{units}; margin:auto 0;')

def centered(a, width, height, xunits='px', yunits='px'):
    return a.div(style=f'width:{width}{xunits}; height:{height}{yunits}; margin:auto auto;')
