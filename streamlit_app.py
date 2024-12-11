import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(data, size=10, border=4, fill_color='black', back_color='white'):
    """
    Generate a QR code with customizable parameters.
    
    :param data: The text/URL to encode in the QR code
    :param size: QR code size (default 10)
    :param border: Border size (default 4)
    :param fill_color: Color of the QR code (default black)
    :param back_color: Background color (default white)
    :return: PIL Image of the QR code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    return qr_image

def main():
    # Set page title and icon
    st.set_page_config(page_title="QR Code Generator", page_icon="🔲")
    
    # Title and description
    st.title("🔲 QR Code Generator")
    st.write("Create custom QR codes with easy-to-use settings!")
    
    # Input form
    with st.form("qr_code_form"):
        # Data input
        data = st.text_input("Enter text or URL", placeholder="https://example.com")
        
        # Customization options
        col1, col2 = st.columns(2)
        
        with col1:
            size = st.slider("QR Code Size", min_value=5, max_value=20, value=10, 
                             help="Adjust the size of each box in the QR code")
            fill_color = st.color_picker("QR Code Color", value="#000000")
        
        with col2:
            border = st.slider("Border Size", min_value=1, max_value=10, value=4,
                               help="Adjust the white space around the QR code")
            back_color = st.color_picker("Background Color", value="#FFFFFF")
        
        # Submit button
        submitted = st.form_submit_button("Generate QR Code")
    
    # Generate and display QR code
    if submitted:
        if not data:
            st.error("Please enter some text or a URL")
        else:
            try:
                # Generate QR code
                qr_image = generate_qr_code(
                    data, 
                    size=size, 
                    border=border, 
                    fill_color=fill_color, 
                    back_color=back_color
                )
                
                # Display QR code
                st.image(qr_image, caption="Generated QR Code", use_column_width=True)
                
                # Download button
                buffered = io.BytesIO()
                qr_image.save(buffered, format="PNG")
                img_bytes = buffered.getvalue()
                
                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qr_code.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
