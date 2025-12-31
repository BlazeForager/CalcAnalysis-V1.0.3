import streamlit as st
import sympy as sp
from CalcModule import CalculusCalculator

# Page Configuration
st.set_page_config(
    page_title="Calculus Analysis Module 1.2",
    page_icon="∫",
    layout="wide"
)

st.image("https://strictlysokudo.com/cdn/shop/files/54PSYDUCK_c0c77920-3da9-41b1-907c-9e6d1b4eb787.png?v=1733536969&width=1445", width=50)
st.title("Calculus Analysis Module")
st.markdown("Perform symbolic calculus operations with ease. Engineered by a team of 3 hardworking psyducks.")

# Initialize Calculator
calc = CalculusCalculator()

# Sidebar: Inputs
st.sidebar.header("Input Settings")
expr_input = st.sidebar.text_input("Expression", "sin(x)**2 + x**2")
var_input = st.sidebar.text_input("Variable", "x")

# Sidebar: Parse Inputs
try:
    if not expr_input:
        st.warning("Please enter an expression.")
        st.stop()
        
    if not var_input:
         st.warning("Please enter a variable.")
         st.stop()
         
    # Parse expression and variable
    sym_var = sp.symbols(var_input)
    sym_expr = sp.sympify(expr_input)
    
    st.sidebar.success("Expression converted successfully!")
    st.sidebar.latex(sp.latex(sym_expr))
    
except sp.SympifyError:
    st.sidebar.error("Invalid expression. Please check Python syntax.")
    st.stop()
except ValueError as e:
    st.sidebar.error(f"Error: {e}")
    st.stop()

# Main Area: Operations
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Differentiation", 
    "Integration", 
    "Limit", 
    "Taylor Series", 
    "Evaluation"
])

# Tab 1: Differentiation
with tab1:
    st.header("Symbolic Differentiation")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        diff_order = st.number_input("Order", min_value=1, max_value=10, value=1, step=1)
        
    if st.button("Calculate Derivative"):
        result = calc.differentiate(sym_expr, sym_var, diff_order)
        st.subheader("Result")
        st.latex(f"\\frac{{d^{{{diff_order}}}}}{{d{var_input}^{{{diff_order}}}}} \\left( {sp.latex(sym_expr)} \\right) = {sp.latex(result)}")

# Tab 2: Integration
with tab2:
    st.header("Symbolic Integration")
    
    integ_type = st.radio("Integration Type", ["Indefinite", "Definite"])
    
    if integ_type == "Definite":
        col1, col2 = st.columns(2)
        with col1:
            lower_bound_str = st.text_input("Lower Bound", "0")
        with col2:
            upper_bound_str = st.text_input("Upper Bound", "1")
        
        if st.button("Calculate Definite Integral"):
            try:
                # Parse bounds
                lower = sp.sympify(lower_bound_str)
                upper = sp.sympify(upper_bound_str)
                result = calc.integrate(sym_expr, sym_var, lower, upper)
                st.subheader("Result")
                st.latex(f"\\int_{{{sp.latex(lower)}}}^{{{sp.latex(upper)}}} {sp.latex(sym_expr)} \\, d{var_input} = {sp.latex(result)}")
            except Exception as e:
                st.error(f"Error parsing bounds: {e}")
    else:
        if st.button("Calculate Indefinite Integral"):
            result = calc.integrate(sym_expr, sym_var)
            st.subheader("Result")
            st.latex(f"\\int {sp.latex(sym_expr)} \\, d{var_input} = {sp.latex(result)} + C")

# Tab 3: Limits
with tab3:
    st.header("Limit Computation")
    
    col1, col2 = st.columns(2)
    with col1:
        point_str = st.text_input("Approach Point", "0")
    with col2:
        direction = st.selectbox("Direction", ["+", "-", "+-"], index=2)
    
    if st.button("Calculate Limit"):
        try:
            point = sp.sympify(point_str)
            result = calc.limit(sym_expr, sym_var, point, direction)
            
            dir_str = ""
            if direction == "+": dir_str = "^+"
            elif direction == "-": dir_str = "^-"
            
            st.subheader("Result")
            st.latex(f"\\lim_{{{var_input} \\to {sp.latex(point)}{dir_str}}} \\left( {sp.latex(sym_expr)} \\right) = {sp.latex(result)}")
        except Exception as e:
            st.error(f"Error calculating limit: {e}")

# Tab 4: Taylor Series
with tab4:
    st.header("Taylor Series Expansion")
    
    col1, col2 = st.columns(2)
    with col1:
        center_str = st.text_input("Expansion Point (Center)", "0")
    with col2:
        order = st.number_input("Order (O(x^n))", min_value=1, max_value=20, value=6)
        
    if st.button("Compute Series"):
        try:
            center = sp.sympify(center_str)
            result = calc.taylor(sym_expr, sym_var, center, order)
            st.subheader("Result")
            st.latex(f"Taylor({sp.latex(sym_expr)}, {var_input}={sp.latex(center)}, {order}) = {sp.latex(result)}")
        except Exception as e:
             st.error(f"Error computing series: {e}")

# Tab 5: Evaluation
with tab5:
    st.header("Numeric Evaluation")
    
    sub_val_str = st.text_input(f"Value for {var_input}", "1")
    
    if st.button("Evaluate"):
        try:
            sub_val = sp.sympify(sub_val_str)
            # Create substitution dictionary
            subs = {sym_var: sub_val}
            result = calc.evaluate(sym_expr, subs)
            st.subheader("Result")
            st.write(f"At {var_input} = {sub_val_str}:")
            st.code(str(result))
        except Exception as e:
            st.error(f"Error evaluating expression: {e}")