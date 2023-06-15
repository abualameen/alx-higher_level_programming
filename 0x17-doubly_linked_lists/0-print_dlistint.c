#include "lists.h"
/**
 * print_dlistint - the func print d val of the nodes in a doubly linked list
 * @h: pointer to the head node
 * Return: data in the nodes
 */



size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *latest = h;
	int counter = 0;

	while (latest != NULL)
	{
		printf("%d \n", latest->n);
		counter++;
		latest = latest->next;
	}
	return (counter);
}
