<?php

/*
// checking count() performance

$a = array_fill(0, 10000, 'test');

$counts = array(10000, 1000000, 10000000);

foreach($counts as $count){
    print "Checking $count \n";
    $time = microtime(true);
    for ($i = 0; $i < $count; $i++)
        if(count($a) > 0){};
    $taken = microtime(true) - $time;
    print "Using count(): $taken ms \n";

    $time = microtime(true);
    $cnt = count($a);
    for ($i = 0; $i < $count; $i++)
        if($cnt > 0){};
    $taken = microtime(true) - $time;
    print "Using \$cnt: $taken ms \n\n";
}

die;

*/


/*

  A
 / \
B   C
   / \
  D   E
   \
    F

Print: A C D F

*/

class Node
{
    public $id;
    public $left;
    public $right;
    public $data;

    public function __construct($id, $data = null)
    {
        $this->id   = $id;
        $this->data = $data;

    }

}

class Tree
{

    const PLACE_LEFT  = 1;
    const PLACE_RIGHT = 2;

    public $root = null;
    public $items = array();

    public function __construct()
    {

    }

    public function add($node, $parent = null, $place = self::PLACE_LEFT)
    {
        if ($parent == null)
            $this->root = $node;
        else {
            if ($place == self::PLACE_LEFT)
                $parent->left = $node;
            else if ($place == self::PLACE_RIGHT)
                $parent->right = $node;
        }

        return $this;

    }
}

function printBranch($nodes)
{
    foreach ($nodes as $node) {
        print $node->id;
        print " ";
    }

    print "\n";
}

$tree = new Tree();

$a = new Node('A');
$b = new Node('B');
$c = new Node('C');
$d = new Node('D');
$e = new Node('E');
$f = new Node('F');

$tree
    ->add($a)
    ->add($b, $a, Tree::PLACE_LEFT)
    ->add($c, $a, Tree::PLACE_RIGHT)
    ->add($d, $c, Tree::PLACE_LEFT)
    ->add($e, $c, Tree::PLACE_RIGHT)
    ->add($f, $d, Tree::PLACE_RIGHT);


function getMaxBranchRecursion($node, $maxBranch = array(), $currentBranch = array())
{
    if (empty($node))
        return;

    $currentBranch[] = $node;
    if (count($currentBranch) > count($maxBranch))
        $maxBranch = $currentBranch;


    if ($node->left)
        $maxBranch = getMaxBranchRecursion($node->left, $maxBranch, $currentBranch);

    if ($node->right)
        $maxBranch = getMaxBranchRecursion($node->right, $maxBranch, $currentBranch);

    return $maxBranch;

}

$maxBranch = getMaxBranchRecursion($tree->root);
print "Recursion:\n";
printBranch( $maxBranch);

function getMaxBranchIter($rootNode)
{

    $node = $rootNode;

    if (empty($node))
        return array();

    $maxBranch     = array($node);
    $currentBranch = array($node);
    $checked       = array();


    while (true) {

        if (count($currentBranch) > count($maxBranch)) {
            $maxBranch = $currentBranch;
        }
        if ($node->left && empty($checked[$node->id]['left'])) {
            $checked[$node->id]['left'] = true;
            $node                       = $node->left;
            $currentBranch[]            = $node;
        } else if ($node->right && empty($checked[$node->id]['right'])) {
            $checked[$node->id]['right'] = true;
            $node                        = $node->right;
            $currentBranch[]             = $node;
        } else {
            if (count($currentBranch) <= 1)
                return $maxBranch;
            array_pop($currentBranch);
            $node = $currentBranch[count($currentBranch) - 1];
        }

    }


}

print "Iteration:\n";
$maxBranch = getMaxBranchIter($tree->root);
printBranch($maxBranch);
