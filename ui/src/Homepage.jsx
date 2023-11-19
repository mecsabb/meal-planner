import React from 'react';
import { Overlay, Title, Button, Space, Group, Center, Container, Text} from '@mantine/core';
import './Homepage.css'
function Homepage() {
    return (
        <Container size={'100%'}>
            <Title className='title'>
                MuckTent
            </Title>
            <Text className='text'>
                Customize your meal preferences, or generate meal recommendations
            </Text>
            <Group className='button-container' gap={'xl'}>
                <Button size='xs' variant='light'>
                    Meal Preferences
                </Button>
                <Button size='xs' variant='light'>
                    Generate Meals
                </Button>
            </Group>
        </Container>
    );
}

export default Homepage