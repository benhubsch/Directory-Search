import click

def test1():
    value = input('What is your greatest fear?')
    return value
def test2():
    color = input('Pick a color')
    return color



# def main():
if __name__ == '__main__':
    click.echo(test1())
    click.echo(test2())
    print('hello')