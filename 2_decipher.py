encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoded_parts = []

for fragment in encoded.split("|"):
    fragment = fragment.strip()

    if fragment.startswith("[") and fragment.endswith("]"):
        fragment = fragment[1:-1]
        parts = fragment.split("::")

        if len(parts) == 3:
            number_text = parts[0]
            jumbled_text = parts[1]
            status = parts[2]

            if number_text.isdigit() and status == "ok":
                number = int(number_text)
                decoded_text = ""

                for character in jumbled_text:
                    if character in alphabet:
                        old_position = alphabet.find(character)
                        new_position = (old_position - number) % len(alphabet)
                        decoded_text = decoded_text + alphabet[new_position]
                    elif character == "_":
                        decoded_text = decoded_text + " "
                    else:
                        decoded_text = decoded_text + character

                decoded_parts.append((number, decoded_text))

decoded_parts.sort()
message_parts = []

for part in decoded_parts:
    message_parts.append(part[1])

final_message = " ".join(message_parts)

print(final_message)
