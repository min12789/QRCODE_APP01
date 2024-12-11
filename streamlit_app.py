    # Generate QR Code
    if st.button('Generate QR Code'):
        if qr_data:
            try:
                # Generate QR Code
                qr_img = generate_qr_code(
                    qr_data, 
                    fill_color=fill_color, 
                    back_color=back_color, 
                    box_size=box_size, 
                    border=border
                )
                
                # Display QR Code
                st.image(qr_img, caption='Generated QR Code', use_column_width='always')
                
                # Download button
                buffered = io.BytesIO()
                qr_img.save(buffered, format="PNG")
                img_bytes = buffered.getvalue()
                
                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qr_code.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Error generating QR Code: {e}")
        else:
            st.warning('Please enter text or a URL')

if __name__ == '__main__':
    main()
