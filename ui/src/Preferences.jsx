import React from 'react';
import {  Button, MantineProvider} from '@mantine/core';

function Preferences() {
    return (
        <MantineProvider>
        <Button>
            Preferences (i feel extra hungry)
        </Button>
        </MantineProvider>
    );
}

export default Preferences

