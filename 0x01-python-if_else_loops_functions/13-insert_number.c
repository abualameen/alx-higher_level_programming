#include "lists.h"
/**
 * add_nodeint - add new nodes at the begining of a list
 * @head: the head of the link list
 * @n:  int data
 * Return: addr
 */
listint_t *insert_node(listint_t **head, int number)
{
	int n = number;
	listint_t *node_new;

	node_new = malloc(sizeof(listint_t));
	if (node_new == NULL)
	{
		return (NULL);
	}
	(*node_new).n = n;
	(*node_new).next = *head;
	*head = node_new;
	return (node_new);
}
