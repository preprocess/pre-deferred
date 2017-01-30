<?php

namespace Pre\Deferred;

use PHPUnit\Framework\TestCase;

class MacroTest extends TestCase
{
    public function testDeferred()
    {
        $fixture = new Fixture\Fixture();

        $this->assertFalse(file_exists(__DIR__ . "/Fixture/touched"));

        $this->assertTrue($fixture->touch());

        $this->assertFalse(file_exists(__DIR__ . "/Fixture/touched"));
    }
}
