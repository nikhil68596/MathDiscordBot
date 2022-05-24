import array
import collections
from collections import deque
import asyncio
from turtle import dot
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import numpy as np

matrix = None
vector = None

load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVERID = os.getenv('ID')

bot = commands.Bot(command_prefix = '$')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} is now ready to work!')

@bot.event
async def on_message(message):
    if(message == 'test'):
        print('Hello World')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    userName = ctx.message.author.name
    await ctx.reply(f'Hello {userName}!')

@bot.command()
async def createMatrix(ctx, length:int, width:int, listOfEntries:str):
    #Create a queue.
    queue = deque()
    listEntr = listOfEntries.split(" ")
    #For each entry
    for entry in listEntr:
        #Access it and put it in the queue.
        queue.append(int(entry))
    #Do this process length by width times
    for i in range(length):
        for j in range(width):
             #If the queue is empty during this process
            if(len(queue) == 0):
                # Return to the user: "You have entered less entries than you are
                # supposed to. Please enter length * width entries".
                await ctx.send(f'You have entered less entries than you are supposed to. Please enter {length * width} entries.')
                return
            queue.pop()
    # If the queue isn't empty
    if(len(queue) != 0):
        # Return to the user: "You have entered more entries than you are
        # supposed to. Please enter length * width entries".
        await ctx.send(f'You have entered more entries than you are supposed to. Please enter {length * width} entries.')
        return
    # Set the matrix instance variable equal to an empty []
    matrix = []
    count = 0
    # For each row
    for i in range(length):
        # Create a vector for that matrix.
        vectorOfMatrix = []
        # For each column
        for j in range(0, width):
            # Read each entry and append it to the row vector.
            vectorOfMatrix.append(listEntr[count])
            count = count + 1
        # Append the row vector to the matrix.
        matrix.append(vectorOfMatrix)
    # Return the matrix to the user.
    await ctx.reply(matrix)
    return matrix

@bot.command()
async def createVector(ctx, length: int, listOfEntries:str):
    #Create a queue.
    queue = deque()
    listEntr = listOfEntries.split(" ")
    #For each entry
    for i in range(0, len(listEntr)):
        #Access it and put it in the queue.
        queue.append(listEntr[i])
    #Do this process length times
    for i in range(length):
        #If the queue is empty during this process
        if(len(queue) == 0):
            # Return to the user: "You have entered less entries than you are
            # supposed to. Please enter length entries".
            await ctx.reply(f'You have entered less entries than you are supposed to. Please enter {length} entries.')
        queue.pop()
    # If the queue isn't empty
    if(len(queue) != 0):
        # Return to the user: "You have entered more entries than you are
        # supposed to. Please enter length * width entries".
        await ctx.reply(f'You have entered more entries than you are supposed to. Please enter {length} entries.')
    # Set the vector instance variable equal to an empty []
    vector = []
    # For each row
    for i in range(0, length):
        # Create a vector for that vector.
        vectorForVector = []
        # Read each entry and append it to the row vector.
        vectorForVector.append(listEntr[i])
        # Append the row vector to the vector.
        vector.append(vectorForVector)
    # Return the vector to the user. 
    await ctx.reply(vector)
    return vector

@bot.command()
async def matrixVectorProduct(ctx, length:int, width:int):
    if(length <= 0 or width <= 0):
        await ctx.reply('Invalid length. Please enter positive arguments for the length and width of the vector you are trying to use to multiply the matrix and vector of a given length and or width.')
        return
    await ctx.send('Enter a list of entries for the matrix.')
    message = await bot.wait_for('message',check=lambda m: m.author==ctx.author and m.channel==ctx.channel,timeout=80)
    createMatrix(ctx, length, width, message)
    await ctx.send('Enter a list of entries for the vector.')
    anotherMessage = await bot.wait_for('message',check=lambda m: m.author==ctx.author and m.channel==ctx.channel,timeout=80)
    createVector(ctx, width,anotherMessage)
    
@bot.command()
async def dotProduct(ctx, length: int):
    if(length <= 0):
        await ctx.reply('Invalid length. Please enter a positive argument for the length of the vector you are trying to use to find the dot product of the vectors.')
        return
    # Create two vectors (vector 1 and vector 2)
    vector1 = []
    vector2 = []
    # For length number of times
    for i in range(length):
        # Create a vector for the first vector
        vectorForVector = []
        # Ask the user to enter the (i, 1) entry of the first vector.
        msg = await ctx.send(f'Please enter the ({i + 1},1) entry of the first vector:')
        # Whatever the user enters, store it in the vector for the first vector.
        message = await bot.wait_for('message',check=lambda m: m.author==ctx.author and m.channel==ctx.channel,timeout=5000)
        entry = None
        try:
            time_to_use = int(message.content)
            entry = time_to_use
        except discord.ext.commands.errors.CommandInvokeError:
            print("The integer Entry is not defined. Please enter an integer entry.")
        except asyncio.TimeoutError:
            await ctx.send("You failed to answer in time or you didn't enter an integer entry.")
        vectorForVector.append(entry)
        # Store that vector for the first vector in the first vector.
        vector1.append(vectorForVector)
        # Repeat the process for the second vector.
        vectorForAnotherVector = []
        # Ask the user to enter the (i, 1) entry of the second vector.
        msg = await ctx.send(f'Please enter the ({i + 1},1) entry of the second vector:')
        # Whatever the user enters, store it in the vector for the second vector.
        message = await bot.wait_for('message',check=lambda m: m.author==ctx.author and m.channel==ctx.channel,timeout=5000)
        entry2 = None
        try:
            time_to_use = int(message.content)
            entry2 = time_to_use
        except asyncio.TimeoutError:
            await ctx.send("You failed to answer in time or you didn't enter an integer entry.")
        vectorForAnotherVector.append(entry2)
        # Store that vector for the first vector in the second vector.
        vector2.append(vectorForAnotherVector)
        # Use a for loop to write the indices after the u and v.
    string = ""
    for i in range(length):
         # Add the + separately.
        string = string + f'u{i+1} * v{i+1}'
        if(i == length-1):
            break
        string = string + " + "
    # Write the formula for the dot product to the user.
    await ctx.send("Dot Product Formula: " + string)
    # Create a string that is empty for now (Used to show work in dot product formula.)
    dotProductWork = ""
    # Have a sum of dot products variable initialized to 0.
    dotProduct = 0
    # For each entry in both vectors [0, length)
    for i in range(length):
        # Get the product of both entries + add it to sum.
        dotProduct = dotProduct + (vector1[i][0] * vector2[i][0])
            # sum += u1 * v1, and so on. 
        # For the string, make sure you type in the entries multiplied at the same index.
        dotProductWork = dotProductWork + f'({vector1[i][0]})({vector2[i][0]})'
        # Check if you reach the last entry to not add the + in the string if you do.
        if(i == length-1):
            break
        else:
            dotProductWork = dotProductWork + " + "
        # Otherwise, add the plus sign in the string. 
    # Return the string being concatenated to equal to the dot product.
    await ctx.send(dotProductWork + f' = {dotProduct}') 
    await ctx.reply(f'The dot product of u and v is {dotProduct}.')
bot.run(TOKEN)