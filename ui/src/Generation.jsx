import React from 'react';
import {  Button, MantineProvider, Card, Group, Text, Image, Stack} from '@mantine/core';
import logo from './assets/sddefault.jpg';
import pancake from './assets/pancake.png';

function Generation() {
    return (
        <MantineProvider>
            <Stack>
            <Card shadow="sm" padding="lg" radius="lg" withBorder height="xl">
                <Card.Section>
                    <Image
                    src={logo}
                    height={160}
                    alt="SM"
                    />
                </Card.Section>

                <Group justify="space-between" mt="md" mb="xs">
                    <Text fw={500}>Spaghetti & Meatballs</Text>
                </Group>

                <Text size="sm" c="dimmed">
                    Can I get the Spaghetti and Meatballs?
                </Text>

                <Button variant="light" color="blue" fullWidth mt="md" radius="md">
                    Buy all new spaghetti meatballs now!!!
                </Button>
            </Card>

            <Card shadow="sm" padding="lg" radius="lg" withBorder>
                <Card.Section>
                    <Image
                    src={pancake}
                    height={160}
                    alt="P"
                    />
                </Card.Section>

                <Group justify="space-between" mt="md" mb="xs">
                    <Text fw={500}>Pancake</Text>
                </Group>

                <Text size="sm" c="dimmed">
                    How about the Pancakes?
                </Text>

                <Button variant="light" color="blue" fullWidth mt="md" radius="md">
                    Fluffy and Delightful!
                </Button>
            </Card>
            </Stack>
        </MantineProvider>
    );
}

export default Generation

