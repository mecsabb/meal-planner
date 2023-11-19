import React from 'react';
import {  Button, Card, MantineProvider, Group, Stack, Image} from '@mantine/core';
import logo from './assets/sddefault.jpg';

function yesEvent() {
    
}

function noEvent() {

}

const meals = {
    
}

function Preferences() {
    return (
        <MantineProvider>
            <Stack>
                <Image src={logo}>

                </Image>
                <Group justify='center' gap={'xl'} grow>
                    <Button color='green' variant='light' size='xl' onClick={yesEvent}>
                        Yes
                    </Button>
                    <Button color='red' variant='light' size='xl' onClick={noEvent}>
                        No
                    </Button>
                </Group>
            </Stack>
        </MantineProvider>
    );
}

export default Preferences

