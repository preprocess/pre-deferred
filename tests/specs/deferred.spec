--DESCRIPTION--

Test deferred

--GIVEN--

defer unlink("path/to/file");

defer {
    fclose($handle);
    print "all done";
}

--EXPECT--

$deferred·0 = new \Pre\Deferred\Deferred(call_user_func(function () {
    $context·0 = func_get_args();

    return function () use ($context·0) {
        call_user_func_array('unlink', $context·0);
    };
}, "path/to/file"));

$deferred·1 = new \Pre\Deferred\Deferred(call_user_func(function ($context·1) {
    return function () use ($context·1) {
        extract($context·1);
        fclose($handle);
        print "all done";
    };
}, get_defined_vars()));
