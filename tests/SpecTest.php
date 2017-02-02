<?php

namespace Pre\Deferred;

use Pre\Testing\Runner;

class SpecTest extends Runner
{
    protected function path(): string
    {
        return __DIR__ . "/specs";
    }
}
