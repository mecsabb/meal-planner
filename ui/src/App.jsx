import { useState } from 'react'
import '@mantine/core/styles.css';
import { MantineProvider, Button, Container, Space, Title, Group, Text } from '@mantine/core';
import './homepage.css'
import './App.css'

function App() {

  return (
    <MantineProvider>
      <div className='container'>
      <Container size={'100%'}>
            <Title className='title'>
                MealMap
            </Title>
            <Text className='text'>
                Customize your meal preferences, or generate meal recommendations
            </Text>
            <Group className='button-container' gap={'xl'}>
                <Button size='xl' variant='light' component='a' href='/preferences'>
                    Meal Preferences
                </Button>
                <Button size='xl' variant='light' component='a' href='/generation'>
                    Generate Meals
                </Button>
            </Group>
        </Container>
      </div>
    </MantineProvider>
  )
}

export default App
