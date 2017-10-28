defer unlink("path/to/file");

~~~

$deferred·0 = new \Pre\Deferred\Deferred((function (...$parameters) {
    return function () use ($parameters) {
        unlink(...$parameters);
    };
})("path/to/file"));

---

defer {
    fclose($handle);
    print "all done";
}

~~~

$deferred·0 = new \Pre\Deferred\Deferred([$handle = $handle ?? null, "fn" => function () use (&$handle) {
    fclose($handle);
    print "all done";
}]["fn"]);
