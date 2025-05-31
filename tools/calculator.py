"""Calculator tool for mathematical operations."""

import ast
import operator
from typing import Dict, Any, Union


class CalculatorTool:
    """Safe calculator tool for mathematical operations."""
    
    # Supported operations
    OPERATIONS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    def calculate(self, expression: str) -> Union[float, str]:
        """Safely evaluate a mathematical expression."""
        try:
            # Parse the expression
            node = ast.parse(expression, mode='eval')
            return self._eval_node(node.body)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _eval_node(self, node):
        """Recursively evaluate AST nodes."""
        if isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        elif isinstance(node, ast.Num):  # Python < 3.8
            return node.n
        elif isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return self.OPERATIONS[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            return self.OPERATIONS[type(node.op)](operand)
        else:
            raise ValueError(f"Unsupported operation: {type(node)}")
    
    def get_function_definition(self) -> Dict[str, Any]:
        """Get the function definition for the LLM."""
        return {
            "name": "calculator",
            "description": "Perform mathematical calculations. Supports +, -, *, /, ** (power), and parentheses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate (e.g., '2 + 3 * 4', '(10 + 5) / 3', '2 ** 3')"
                    }
                },
                "required": ["expression"]
            }
        }


# Create a global instance
calculator_tool = CalculatorTool() 