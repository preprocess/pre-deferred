<?php

namespace Pre\Deferred;

final class Deferred
{
    private $deferred;

    public function __construct(callable $deferred)
    {
        $this->deferred = $deferred;
    }

    public function __destruct()
    {
        call_user_func($this->deferred);
    }
}
