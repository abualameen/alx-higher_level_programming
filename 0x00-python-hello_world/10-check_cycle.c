#include "lists.h"
/*
 * floyd_algo - detects if there is loop in linked list
 * @head: pointer to the head node
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;
	while (fast != NULL && (*fast).next != NULL)
	{
		slow = (*slow).next;
		fast = fast->next->next;
		if (slow == fast)
		{
			break;
		}
	}
	if (fast == NULL || fast->next == NULL)
	{
		return (0);
	}
	slow = list;
	while (slow != fast)
	{
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
