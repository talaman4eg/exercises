<?php


class Node {

	public $value;
	public $next;


	public static function create($value = null, $next = null) {
		$node = new Node();
		$node->value = $value;
		$node->next = $next;
		return $node;
	}

	public static function isNode($node){
		return !empty($node) && is_a($node, 'Node') && ($node->next || $node->value);
	}

	public static function flattern(Node &$node){
		if (!Node::isNode($node))
			return false;

		if (Node::isNode($node->value)){
			print 'eoc: '.$eoc->value;
			$eoc = Node::flattern($node->value);
			$eoc->next = $node->next;
			$node = $node->value;
		}
		if(Node::isNode($node->next)){
			return Node::flattern($node->next);
		}else{
			return $node;
		}
	}

	public static function printList(Node $node){
		if (Node::isNode($node->value)){
			echo 'Node ( ';
			Node::printList($node->value);
			echo ' )';
		} else {
			echo "Node ({$node->value})";
		}
		if(Node::isNode($node->next)){
			print("->");
			Node::printList($node->next);
		}		
	}

}

$nodes = array(
		Node::create(0),
		Node::create(1),
		Node::create(2),
		Node::create(3),
		Node::create(4),
		Node::create(5),
		Node::create(6),
		Node::create(7),
		Node::create(8),
		Node::create(9),
	);
$nodes[0]->next = $nodes[1];
$nodes[1]->next = $nodes[2];
$nodes[2]->next = $nodes[3];
$nodes[3]->value = $nodes[4];
$nodes[4]->next = $nodes[5];
$nodes[5]->value = $nodes[6];
$nodes[3]->next = $nodes[7];
$nodes[4]->value = $nodes[8];
$nodes[8]->next = $nodes[9];
Node::printList($nodes[0]);
print '<br />';
Node::flattern($nodes[0]);
print '<br />';
Node::printList($nodes[0]);


