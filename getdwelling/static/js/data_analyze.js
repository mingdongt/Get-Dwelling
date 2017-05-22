/**
 * Created by mingdongtan on 18/5/17.
 */


$("select").select2({
        dropdownCssClass: 'dropdown-inverse',
        placeholder: "   (Optional)"
    });

$(document).ready(function () {
    $(".unique-dropdown").each(function () {
        var $self = $(this);
        $self.data("previous_value", $self.val());
    });

    $(".unique-dropdown").on("change", function () {
        var $self = $(this);
        var prev_value = $self.data("previous_value");
        var cur_value = $self.val();

        $(".unique-dropdown").not($self).find("option").filter(function () {
            return $(this).val() == prev_value;
        }).prop("disabled", false);

        if (cur_value != "") {
            $(".unique-dropdown").not($self).find("option").filter(function () {
                return $(this).val() == cur_value;
            }).prop("disabled", true);

            $self.data("previous_value", cur_value);
        }
    });
});
