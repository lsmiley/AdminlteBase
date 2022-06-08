<!--This is a repository of Random and Base Scripts for future use-->
<!--This File is not to be Called by any Action or Process-->





<!-- Product #1 Calc -->
<script type="text/javascript">
    $(function () {
        $("#AvProductId").change(function () {
          //  alert($(this).val() + " " + $(this).find("option:selected").html());
            var id = $(this).val();
            $.ajax({
                type: "Post",
                url: '@Url.Action("GetProductByID1", "SizingUserDashBoard")',
                data: '{id: "' + id + '"}',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (data) {
                    //alert(data.LastName);

                    $("#TestProdDesc13").val(data.Component13Desc);
                    $("#Prod1Compnent2Desc").val($("#txtComponent2Desc1").val());
                    $("#Prod1Compnent3Desc").val($("#txtComponent3Desc1").val());*@

                    //$("#TestProdDesc12").val($("#txtComponent12Desc1").val());
                    //$("#TestProdDesc13").val($("#txtComponent13Desc1").val());

                    $("#DescProduct_1").val(data.ProductName);
                    $("#Prod1Compnent1Desc").val(data.Component1Desc);
                    $("#Prod1Compnent2Desc").val(data.Component2Desc);
                    $("#Prod1Compnent3Desc").val(data.Component3Desc);
                    $("#Prod1Compnent4Desc").val(data.Component4Desc);
                    $("#Prod1Compnent5Desc").val(data.Component5Desc);

                    $("#Prod1Compnent6Desc").val(data.Component6Desc);
                    $("#Prod1Compnent7Desc").val(data.Component7Desc);
                    $("#Prod1Compnent8Desc").val(data.Component8Desc);
                    $("#Prod1Compnent9Desc").val(data.Component9Desc);
                    $("#Prod1Compnent10Desc").val(data.Component10Desc);

                    $("#Prod1Compnent11Desc").val(data.Component11Desc);
                    $("#Prod1Compnent12Desc").val(data.Component12Desc);
                    $("#Prod1Compnent13Desc").val(data.Component13Desc);
                    $("#Prod1Compnent14Desc").val(data.Component14Desc);
                    $("#Prod1Compnent15Desc").val(data.Component15Desc);


                    $("#Compnent1Desc").val(data.Component1Desc);
                    $("#Compnent2Desc").val(data.Component2Desc);
                    $("#Compnent3Desc").val(data.Component3Desc);
                    $("#Compnent4Desc").val(data.Component4Desc);
                    $("#Compnent5Desc").val(data.Component5Desc);
                    $("#Compnent6Desc").val(data.Component6Desc);
                    $("#Compnent7Desc").val(data.Component7Desc);
                    $("#Compnent8Desc").val(data.Component8Desc);
                    $("#Compnent9Desc").val(data.Component9Desc);
                    $("#Compnent10Desc").val(data.Component10Desc);
                    $("#Compnent11Desc").val(data.Component11Desc);
                    $("#Compnent12Desc").val(data.Component12Desc);
                    $("#Compnent13Desc").val(data.Component13Desc);
                    $("#Compnent14Desc").val(data.Component14Desc);
                    $("#Compnent15Desc").val(data.Component15Desc);

                    $("#Prod1ComponentComplexityFac1_1").val(data.ComponentComplexityFac1);
                    $("#Prod1ComponentComplexityFac2_1").val(data.ComponentComplexityFac2);
                    $("#Prod1ComponentComplexityFac3_1").val(data.ComponentComplexityFac3);
                    $("#Prod1ComponentComplexityFac4_1").val(data.ComponentComplexityFac4);
                    $("#Prod1ComponentComplexityFac5_1").val(data.ComponentComplexityFac5);
                    $("#Prod1ComponentComplexityFac6_1").val(data.ComponentComplexityFac6);
                    $("#Prod1ComponentComplexityFac7_1").val(data.ComponentComplexityFac7);
                    $("#Prod1ComponentComplexityFac8_1").val(data.ComponentComplexityFac8);
                    $("#Prod1ComponentComplexityFac9_1").val(data.ComponentComplexityFac9);
                    $("#Prod1ComponentComplexityFac10_1").val(data.ComponentComplexityFac10);
                    $("#Prod1ComponentComplexityFac11_1").val(data.ComponentComplexityFac11);
                    $("#Prod1ComponentComplexityFac12_1").val(data.ComponentComplexityFac12);
                    $("#Prod1ComponentComplexityFac13_1").val(data.ComponentComplexityFac13);
                    $("#Prod1ComponentComplexityFac14_1").val(data.ComponentComplexityFac14);
                    $("#Prod1ComponentComplexityFac15_1").val(data.ComponentComplexityFac15);



                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Failed to retrieve Products.');
                }
            });

        });
    });
</script>



<!--Code to Clear Products and Delivery Centers-->

<!--Product# 1-->

<script type="text/javascript">
    $(document).ready(function () {
        $("#ClearData").click(function () {

            $("#AvProduct.Component1Desc")[0].value = "";
            $("#Component2Desc")[0].value = "";
            $("#Component3Desc")[0].value = "";
            $("#Component4Desc")[0].value = "";
            $("#Component5Desc")[0].value = "";

            $("#Component6Desc")[0].value = "";
            $("#Component7Desc")[0].value = "";
            $("#Component8Desc")[0].value = "";
            $("#Component9Desc")[0].value = "";
            $("#Component10Desc")[0].value = "";

            $("#Component11Desc")[0].value = "";
            $("#Component12Desc")[0].value = "";
            $("#Component13Desc")[0].value = "";
            $("#Component14Desc")[0].value = "";
            $("#Component15Desc")[0].value = "";


            $("#Prod1Component1_Wkstn").prop("checked", false);
            $("#Prod1Component2_Wkstn").prop("checked", false);
            $("#Prod1Component3_Wkstn").prop("checked", false);
            $("#Prod1Component4_Wkstn").prop("checked", false);
            $("#Prod1Component5_Wkstn").prop("checked", false);

            $("#Prod1Component6_Wkstn").prop("checked", false);
            $("#Prod1Component7_Wkstn").prop("checked", false);
            $("#Prod1Component8_Wkstn").prop("checked", false);
            $("#Prod1Component9_Wkstn").prop("checked", false);
            $("#Prod1Component10_Wkstn").prop("checked", false);

            $("#Prod1Component11_Wkstn").prop("checked", false);
            $("#Prod1Component12_Wkstn").prop("checked", false);
            $("#Prod1Component13_Wkstn").prop("checked", false);
            $("#Prod1Component14_Wkstn").prop("checked", false);
            $("#Prod1Component15_Wkstn").prop("checked", false);

            $("#Prod1Component1_Svr").prop("checked", false);
            $("#Prod1Component2_Svr").prop("checked", false);
            $("#Prod1Component3_Svr").prop("checked", false);
            $("#Prod1Component4_Svr").prop("checked", false);
            $("#Prod1Component5_Svr").prop("checked", false);

            $("#Prod1Component6_Svr").prop("checked", false);
            $("#Prod1Component7_Svr").prop("checked", false);
            $("#Prod1Component8_Svr").prop("checked", false);
            $("#Prod1Component9_Svr").prop("checked", false);
            $("#Prod1Component10_Svr").prop("checked", false);

            $("#Prod1Component11_Svr").prop("checked", false);
            $("#Prod1Component12_Svr").prop("checked", false);
            $("#Prod1Component13_Svr").prop("checked", false);
            $("#Prod1Component14_Svr").prop("checked", false);
            $("#Prod1Component15_Svr").prop("checked", false);

            $("#Prod1Component1_IP").prop("checked", false);
            $("#Prod1Component2_IP").prop("checked", false);
            $("#Prod1Component3_IP").prop("checked", false);
            $("#Prod1Component4_IP").prop("checked", false);
            $("#Prod1Component5_IP").prop("checked", false);

            $("#Prod1Component6_IP").prop("checked", false);
            $("#Prod1Component7_IP").prop("checked", false);
            $("#Prod1Component8_IP").prop("checked", false);
            $("#Prod1Component9_IP").prop("checked", false);
            $("#Prod1Component10_IP").prop("checked", false);

            $("#Prod1Component11_IP").prop("checked", false);
            $("#Prod1Component12_IP").prop("checked", false);
            $("#Prod1Component13_IP").prop("checked", false);
            $("#Prod1Component14_IP").prop("checked", false);
            $("#Prod1Component15_IP").prop("checked", false);


            $("#Prod1Component_Qty1")[0].value = 0;
            $("#Prod1Component_Qty2")[0].value = 0;
            $("#Prod1Component_Qty3")[0].value = 0;
            $("#Prod1Component_Qty4")[0].value = 0;
            $("#Prod1Component_Qty5")[0].value = 0;

            $("#Prod1Component_Qty6")[0].value = 0;
            $("#Prod1Component_Qty7")[0].value = 0;
            $("#Prod1Component_Qty8")[0].value = 0;
            $("#Prod1Component_Qty9")[0].value = 0;
            $("#Prod1Component_Qty10")[0].value = 0;

            $("#Prod1Component_Qty11")[0].value = 0;
            $("#Prod1Component_Qty12")[0].value = 0;
            $("#Prod1Component_Qty13")[0].value = 0;
            $("#Prod1Component_Qty14")[0].value = 0;
            $("#Prod1Component_Qty15")[0].value = 0;
            $("#DescProduct_1")[0].value = "";
            $("#DescLaborDelivery_1")[0].value = "";

            $("#NumWorkstation")[0].value = 0;
            $("#NumServer")[0].value = 0;
            $("#NumIpAddress")[0].value = 0;
            $("#NumAddlCon")[0].value = 0;

            $("#Prod1ComponentHours1")[0].value = 0;
            $("#Prod1ComponentHours2")[0].value = 0;
            $("#Prod1ComponentHours3")[0].value = 0;
            $("#Prod1ComponentHours4")[0].value = 0;
            $("#Prod1ComponentHours5")[0].value = 0;

            $("#Prod1ComponentHours6")[0].value = 0;
            $("#Prod1ComponentHours7")[0].value = 0;
            $("#Prod1ComponentHours8")[0].value = 0;
            $("#Prod1ComponentHours9")[0].value = 0;
            $("#Prod1ComponentHours10")[0].value = 0;

            $("#Prod1ComponentHours11")[0].value = 0;
            $("#Prod1ComponentHours12")[0].value = 0;
            $("#Prod1ComponentHours13")[0].value = 0;
            $("#Prod1ComponentHours14")[0].value = 0;
            $("#`5")[0].value = 0;

            return false;
        });
    });
</script>



<!--LaborDelivery# 1-->
<script type="text/javascript">
    $(function () {
        $("#ddl_DeliveredFrom1").change(function () {
          //  alert($(this).val() + " " + $(this).find("option:selected").html());
            var id = $(this).val();
            $.ajax({
                type: "Post",
                url: '@Url.Action("GetDeliveredFrom1ID", "Dashboard_Old")',
                data: '{id: "' + id + '"}',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (data) {
                    //alert(data.LastName);
                    $("#txtLaborDeliveryId").val(data.LaborDeliveryId);
                    $("#txtRegions").val(data.Regions);
                    $("#txtDefaultFTE_Year").val(data.DefaultFTE_Year);
                    $("#txtWorkWeek").val(data.WorkWeek);
                    $("#txtDeliveryCtrCostFactor").val(data.DeliveryCtrCostFactor);
                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Failed to retrieve Delivery Center.');
                }
            });

        });
    });
</script>


<script type="text/javascript">
    $(function () {
        $("#LaborDeliveryId").change(function () {
          //  alert($(this).val() + " " + $(this).find("option:selected").html());
            var id = $(this).val();
            $.ajax({
                type: "Post",
                url: '@Url.Action("GetLaborByID1", "SizingUserDashboard")',
                data: '{id: "' + id + '"}',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (data) {
                    //alert(data.LastName);
                    //$("#txtLaborId1").val(data.LaborDeliveryId);
                    //$("#txtRegionNumber_1").val(data.RegionNumber);
                    //$("#txtRegions_1").val(data.Regions);
                    //$("#txtDeliveryOption_1").val(data.DeliveryOption);
                    //$("#txtCurrencyType_1").val(data.CurrencyType);

                    DescProduct_1
                    $("#DescLaborDelivery_1").val(data.Regions);
                    $("#Default_Yr_LaborDelivery_1").val(data.DefaultFTE_Year);
                    $("#Prod1WorkWeek").val(data.WorkWeek);
                    $("#DeliveryCtrCostFactor_1").val(data.DeliveryCtrCostFactor);

                    $("#Prod1_Band3_Percentage").val(data.Band3Percentage);
                    $("#Prod1_Band4_Percentage").val(data.Band4Percentage);
                    $("#Prod1_Band5_Percentage").val(data.Band5Percentage);
                    $("#Prod1_Band6_Percentage").val(data.Band6Percentage);
                    $("#Prod1_Band7_Percentage").val(data.Band7Percentage);
                    $("#Prod1_Band8_Percentage").val(data.Band8Percentage);
                    $("#Prod1_Band9_Percentage").val(data.Band9Percentage)

                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Failed to retrieve Labor and Delivery.');
                }
            });

        });
    });
</script>



<!--    Code to Update TntWOrksheet DATA to Fields-->

<!--    Fetch TnTWorkSheet Data-->

<script type="text/javascript">
    $(function () {
        $("#TnTId").change(function () {
          //  alert($(this).val() + " " + $(this).find("option:selected").html());
            var id = $(this).val();
            $.ajax({
                type: "Post",
                url: '@Url.Action("GetTNTByID1", "SizingUserDashboard")',
                data: '{id: "' + id + '"}',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (data) {
                    //alert(data.LastName);
                    $("#TNTId").val(data.TnTId);
                    TnTDescription

                    $("#TnTDescription").val(data.TnTDescription);
                    $("#TotalTransitionHoursItem_BZ").val(data.TotalTransitionHoursItem);
                    $("#TotalTransformationHoursItem_BZ").val(data.TotalTransformationHoursItem);
                    $("#SpecialItem1_TransitionHours").val(data.SpecialItem1_TransitionHours);
                    $("#SpecialItem2_TransitionHours").val(data.SpecialItem2_TransitionHours);
                    $("#SpecialItem3_TransitionHours").val(data.SpecialItem3_TransitionHours);
                    $("#SpecialItem4_TransitionHours").val(data.SpecialItem4_TransitionHours);
                    $("#SpecialItem5_TransitionHours").val(data.SpecialItem5_TransitionHours);
                    //$("#TotalTransitionHoursItem").val(data.TotalTransitionHoursItem);

                    $("#TotalTransformationHoursItem_BZ").val(data.TotalTranformationHoursItem);
                    $("#SpecialItem1_TranformationHours").val(data.SpecialItem1_TranformationHours);
                    $("#SpecialItem2_TranformationHours").val(data.SpecialItem2_TranformationHours);
                    $("#SpecialItem3_TranformationHours").val(data.SpecialItem3_TranformationHours);
                    $("#SpecialItem4_TranformationHours").val(data.SpecialItem4_TranformationHours);
                    $("#SpecialItem5_TranformationHours").val(data.SpecialItem5_TranformationHours);
                    //$("#TotalTransformationHoursItem").val(data.TotalTranformationHoursItem);


                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Failed to retrieve Labor and Delivery.');
                }
            });

        });
    });
</script>



<!-- Code for Primary Tab to maintain Tab Position during Session*@-->
<script type="text/javascript">
    $(document).ready(function () {
        var currentMainTabIndex = "0";

        $tab = $("#tabs").tabs({
            activate: function (e, ui) {
                currentMainTabIndex = ui.newTab.index().toString();
                sessionStorage.setItem('tab-index', currentMainTabIndex);
            }
        });

        if (sessionStorage.getItem('tab-index') != null) {
            currentMainTabIndex = sessionStorage.getItem('tab-index');
            console.log(currentMainTabIndex);
            $tab.tabs('option', 'active', currentMainTabIndex);
        }
        $('#btn-sub').on('click', function () {
            sessionStorage.setItem("tab-index", currentMainTabIndex);
            //window.location = "/Home/Index/";
        });
    });
</script>


<!-- Code for Products Tab to maintain Tab Position during Session*@-->

<script type="text/javascript">
    $(document).ready(function () {
        var currentTabIndex = "0";

        $tab = $("#ProductsViewTabs").tabs({
            activate: function (e, ui) {
                currentTabIndex = ui.newTab.index().toString();
                sessionStorage.setItem('tab-index', currentTabIndex);
            }
        });

        if (sessionStorage.getItem('tab-index') != null) {
            currentTabIndex = sessionStorage.getItem('tab-index');
            console.log(currentTabIndex);
            $tab.tabs('option', 'active', currentTabIndex);
        }
        $('#btn-sub').on('click', function () {
            sessionStorage.setItem("tab-index", currentTabIndex);
            //window.location = "/Home/Index/";
        });
    });
</script>


<!-- Code to Clear Products and Dleivery Centers *@-->

<!-- Product# 1 -->

<script type="text/javascript">
    $(document).ready(function () {
        $("#ClearData").click(function () {

            $("#AvProduct.Component1Desc")[0].value = "";
            $("#Component2Desc")[0].value = "";
            $("#Component3Desc")[0].value = "";
            $("#Component4Desc")[0].value = "";
            $("#Component5Desc")[0].value = "";

            $("#Component6Desc")[0].value = "";
            $("#Component7Desc")[0].value = "";
            $("#Component8Desc")[0].value = "";
            $("#Component9Desc")[0].value = "";
            $("#Component10Desc")[0].value = "";

            $("#Component11Desc")[0].value = "";
            $("#Component12Desc")[0].value = "";
            $("#Component13Desc")[0].value = "";
            $("#Component14Desc")[0].value = "";
            $("#Component15Desc")[0].value = "";


            $("#Prod1Component1_Wkstn").prop("checked", false);
            $("#Prod1Component2_Wkstn").prop("checked", false);
            $("#Prod1Component3_Wkstn").prop("checked", false);
            $("#Prod1Component4_Wkstn").prop("checked", false);
            $("#Prod1Component5_Wkstn").prop("checked", false);

            $("#Prod1Component6_Wkstn").prop("checked", false);
            $("#Prod1Component7_Wkstn").prop("checked", false);
            $("#Prod1Component8_Wkstn").prop("checked", false);
            $("#Prod1Component9_Wkstn").prop("checked", false);
            $("#Prod1Component10_Wkstn").prop("checked", false);

            $("#Prod1Component11_Wkstn").prop("checked", false);
            $("#Prod1Component12_Wkstn").prop("checked", false);
            $("#Prod1Component13_Wkstn").prop("checked", false);
            $("#Prod1Component14_Wkstn").prop("checked", false);
            $("#Prod1Component15_Wkstn").prop("checked", false);

            $("#Prod1Component1_Svr").prop("checked", false);
            $("#Prod1Component2_Svr").prop("checked", false);
            $("#Prod1Component3_Svr").prop("checked", false);
            $("#Prod1Component4_Svr").prop("checked", false);
            $("#Prod1Component5_Svr").prop("checked", false);

            $("#Prod1Component6_Svr").prop("checked", false);
            $("#Prod1Component7_Svr").prop("checked", false);
            $("#Prod1Component8_Svr").prop("checked", false);
            $("#Prod1Component9_Svr").prop("checked", false);
            $("#Prod1Component10_Svr").prop("checked", false);

            $("#Prod1Component11_Svr").prop("checked", false);
            $("#Prod1Component12_Svr").prop("checked", false);
            $("#Prod1Component13_Svr").prop("checked", false);
            $("#Prod1Component14_Svr").prop("checked", false);
            $("#Prod1Component15_Svr").prop("checked", false);

            $("#Prod1Component1_IP").prop("checked", false);
            $("#Prod1Component2_IP").prop("checked", false);
            $("#Prod1Component3_IP").prop("checked", false);
            $("#Prod1Component4_IP").prop("checked", false);
            $("#Prod1Component5_IP").prop("checked", false);

            $("#Prod1Component6_IP").prop("checked", false);
            $("#Prod1Component7_IP").prop("checked", false);
            $("#Prod1Component8_IP").prop("checked", false);
            $("#Prod1Component9_IP").prop("checked", false);
            $("#Prod1Component10_IP").prop("checked", false);

            $("#Prod1Component11_IP").prop("checked", false);
            $("#Prod1Component12_IP").prop("checked", false);
            $("#Prod1Component13_IP").prop("checked", false);
            $("#Prod1Component14_IP").prop("checked", false);
            $("#Prod1Component15_IP").prop("checked", false);


            $("#Prod1Component_Qty1")[0].value = 0;
            $("#Prod1Component_Qty2")[0].value = 0;
            $("#Prod1Component_Qty3")[0].value = 0;
            $("#Prod1Component_Qty4")[0].value = 0;
            $("#Prod1Component_Qty5")[0].value = 0;

            $("#Prod1Component_Qty6")[0].value = 0;
            $("#Prod1Component_Qty7")[0].value = 0;
            $("#Prod1Component_Qty8")[0].value = 0;
            $("#Prod1Component_Qty9")[0].value = 0;
            $("#Prod1Component_Qty10")[0].value = 0;

            $("#Prod1Component_Qty11")[0].value = 0;
            $("#Prod1Component_Qty12")[0].value = 0;
            $("#Prod1Component_Qty13")[0].value = 0;
            $("#Prod1Component_Qty14")[0].value = 0;
            $("#Prod1Component_Qty15")[0].value = 0;
            $("#DescProduct_1")[0].value = "";
            $("#DescLaborDelivery_1")[0].value = "";

            $("#NumWorkstation")[0].value = 0;
            $("#NumServer")[0].value = 0;
            $("#NumIpAddress")[0].value = 0;
            $("#NumAddlCon")[0].value = 0;

            $("#Prod1ComponentHours1")[0].value = 0;
            $("#Prod1ComponentHours2")[0].value = 0;
            $("#Prod1ComponentHours3")[0].value = 0;
            $("#Prod1ComponentHours4")[0].value = 0;
            $("#Prod1ComponentHours5")[0].value = 0;

            $("#Prod1ComponentHours6")[0].value = 0;
            $("#Prod1ComponentHours7")[0].value = 0;
            $("#Prod1ComponentHours8")[0].value = 0;
            $("#Prod1ComponentHours9")[0].value = 0;
            $("#Prod1ComponentHours10")[0].value = 0;

            $("#Prod1ComponentHours11")[0].value = 0;
            $("#Prod1ComponentHours12")[0].value = 0;
            $("#Prod1ComponentHours13")[0].value = 0;
            $("#Prod1ComponentHours14")[0].value = 0;
            $("#`5")[0].value = 0;

            return false;
        });
    });
</script>



<!-- Product#2 ClearData -->

<script type="text/javascript">
    $(document).ready(function () {
        $("#ClearData1").click(function () {

            $("#Prod2Compnent1Desc")[0].value = "";
            $("#Prod2Compnent2Desc")[0].value = "";
            $("#Prod2Compnent3Desc")[0].value = "";
            $("#Prod2Compnent4Desc")[0].value = "";
            $("#Prod2Compnent5Desc")[0].value = "";

            $("#Prod2Compnent6Desc")[0].value = "";
            $("#Prod2Compnent7Desc")[0].value = "";
            $("#Prod2Compnent8Desc")[0].value = "";
            $("#Prod2Compnent9Desc")[0].value = "";
            $("#Prod2Compnent10Desc")[0].value = "";

            $("#Prod2Compnent11Desc")[0].value = "";
            $("#Prod2Compnent12Desc")[0].value = "";
            $("#Prod2Compnent13Desc")[0].value = "";
            $("#Prod2Compnent14Desc")[0].value = "";
            $("#Prod2Compnent15Desc")[0].value = "";


            $("#Prod2Component1_Wkstn").prop("checked", false);
            $("#Prod2Component2_Wkstn").prop("checked", false);
            $("#Prod2Component3_Wkstn").prop("checked", false);
            $("#Prod2Component4_Wkstn").prop("checked", false);
            $("#Prod2Component5_Wkstn").prop("checked", false);

            $("#Prod2Component6_Wkstn").prop("checked", false);
            $("#Prod2Component7_Wkstn").prop("checked", false);
            $("#Prod2Component8_Wkstn").prop("checked", false);
            $("#Prod2Component9_Wkstn").prop("checked", false);
            $("#Prod2Component10_Wkstn").prop("checked", false);

            $("#Prod2Component11_Wkstn").prop("checked", false);
            $("#Prod2Component12_Wkstn").prop("checked", false);
            $("#Prod2Component13_Wkstn").prop("checked", false);
            $("#Prod2Component14_Wkstn").prop("checked", false);
            $("#Prod2Component15_Wkstn").prop("checked", false);

            $("#Prod2Component1_Svr").prop("checked", false);
            $("#Prod2Component2_Svr").prop("checked", false);
            $("#Prod2Component3_Svr").prop("checked", false);
            $("#Prod2Component4_Svr").prop("checked", false);
            $("#Prod2Component5_Svr").prop("checked", false);

            $("#Prod2Component6_Svr").prop("checked", false);
            $("#Prod2Component7_Svr").prop("checked", false);
            $("#Prod2Component8_Svr").prop("checked", false);
            $("#Prod2Component9_Svr").prop("checked", false);
            $("#Prod2Component10_Svr").prop("checked", false);

            $("#Prod2Component11_Svr").prop("checked", false);
            $("#Prod2Component12_Svr").prop("checked", false);
            $("#Prod2Component13_Svr").prop("checked", false);
            $("#Prod2Component14_Svr").prop("checked", false);
            $("#Prod2Component15_Svr").prop("checked", false);

            $("#Prod2Component1_IP").prop("checked", false);
            $("#Prod2Component2_IP").prop("checked", false);
            $("#Prod2Component3_IP").prop("checked", false);
            $("#Prod2Component4_IP").prop("checked", false);
            $("#Prod2Component5_IP").prop("checked", false);

            $("#Prod2Component6_IP").prop("checked", false);
            $("#Prod2Component7_IP").prop("checked", false);
            $("#Prod2Component8_IP").prop("checked", false);
            $("#Prod2Component9_IP").prop("checked", false);
            $("#Prod2Component10_IP").prop("checked", false);

            $("#Prod2Component11_IP").prop("checked", false);
            $("#Prod2Component12_IP").prop("checked", false);
            $("#Prod2Component13_IP").prop("checked", false);
            $("#Prod2Component14_IP").prop("checked", false);
            $("#Prod2Component15_IP").prop("checked", false);


            $("#Prod2Component_Qty1")[0].value = 0;
            $("#Prod2Component_Qty2")[0].value = 0;
            $("#Prod2Component_Qty3")[0].value = 0;
            $("#Prod2Component_Qty4")[0].value = 0;
            $("#Prod2Component_Qty5")[0].value = 0;

            $("#Prod2Component_Qty6")[0].value = 0;
            $("#Prod2Component_Qty7")[0].value = 0;
            $("#Prod2Component_Qty8")[0].value = 0;
            $("#Prod2Component_Qty9")[0].value = 0;
            $("#Prod2Component_Qty10")[0].value = 0;

            $("#Prod2Component_Qty11")[0].value = 0;
            $("#Prod2Component_Qty12")[0].value = 0;
            $("#Prod2Component_Qty13")[0].value = 0;
            $("#Prod2Component_Qty14")[0].value = 0;
            $("#Prod2Component_Qty15")[0].value = 0;
            $("#DescProduct_2")[0].value = "";
            $("#DescLaborDelivery_2")[0].value = "";

            $("#NumWorkstation1")[0].value = 0;
            $("#NumServer1")[0].value = 0;
            $("#NumIpAddress1")[0].value = 0;
            $("#NumAddlCon1")[0].value = 0;
            $("#NumMonths_2")[0].value = 0;

            $("#Prod2ComponentHours1")[0].value = 0;
            $("#Prod2ComponentHours2")[0].value = 0;
            $("#Prod2ComponentHours3")[0].value = 0;
            $("#Prod2ComponentHours4")[0].value = 0;
            $("#Prod2ComponentHours5")[0].value = 0;

            $("#Prod2ComponentHours6")[0].value = 0;
            $("#Prod2ComponentHours7")[0].value = 0;
            $("#Prod2ComponentHours8")[0].value = 0;
            $("#Prod2ComponentHours9")[0].value = 0;
            $("#Prod2ComponentHours10")[0].value = 0;

            $("#Prod2ComponentHours11")[0].value = 0;
            $("#Prod2ComponentHours12")[0].value = 0;
            $("#Prod2ComponentHours13")[0].value = 0;
            $("#Prod2ComponentHours14")[0].value = 0;
            $("#Prod2ComponentHours15")[0].value = 0;

            return false;
        });
    });
</script>




<!--        Cascading Dropdown-->


<script src="~/Scripts/jquery-1.10.2.min.js"></script>

<script type="text/javascript">

$(document).ready(function () {

    $("#ProdCategoryId").change(function () {
        $("#AvProductId").empty();
        $.ajax({
            type: 'POST',
            url: '@Url.Action("GetAvproductCascade")',
            dataType: 'json',
            data: { id: $("#ProdCategoryId").val() },
            success: function (avproduct) {

                $.each(city, function (i, city) {
                    $("#AvProductId").append('<option value="'
                                               + avproduct.Value + '">'
                                         + avproduct.Text + '</option>');
                });
            },
            error: function (ex) {
                alert('Failed.' + ex);
            }
       });
        return false;
    })
});
</script>




<script src="https://code.jquery.com/ui/1.10.4/jquery-ui.min.js"></script>
<script src="~/ckeditor/ckeditor.js"></script>
<script src="~/ckeditor/adapters/jquery.js"></script>


<!-- Code to Block Use of "Enter Key" from saving or entering Records*@-->
<script>
    $(document).keypress(function (e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            return false;
        }
    });
</script>

<!--Style for Slider*@-->
<style>
    body {
        padding-top: 50px;
        padding-bottom: 50px;
    }

    .price-box {
        margin: 0 auto;
        background: #E9E9E9;
        border-radius: 10px;
        padding: 40px 15px;
        width: 500px;
    }

    .ui-widget-content {
        border: 1px solid #bdc3c7;
        background: #e1e1e1;
        color: #222222;
        margin-top: 4px;
    }

    .ui-slider .ui-slider-handle {
        position: absolute;
        z-index: 2;
        width: 5.2em;
        height: 2.2em;
        cursor: default;
        margin: 0 -40px auto !important;
        text-align: center;
        line-height: 30px;
        color: #FFFFFF;
        font-size: 15px;
    }

        .ui-slider .ui-slider-handle .glyphicon {
            color: #FFFFFF;
            margin: 0 3px;
            font-size: 11px;
            opacity: 0.5;
        }

    .ui-corner-all {
        border-radius: 20px;
    }

    .ui-slider-horizontal .ui-slider-handle {
        top: -.9em;
    }

    .ui-state-default,
    .ui-widget-content .ui-state-default {
        border: 1px solid #f9f9f9;
        background: #3498db;
    }

    .ui-slider-horizontal .ui-slider-handle {
        margin-left: -0.5em;
    }

    .ui-slider .ui-slider-handle {
        cursor: pointer;
    }

    .ui-slider a,
    .ui-slider a:focus {
        cursor: pointer;
        outline: none;
    }

    .price, .lead p {
        font-weight: 600;
        font-size: 32px;
        display: inline-block;
        line-height: 60px;
    }

    h4.great {
        background: #00ac98;
        margin: 0 0 25px -60px;
        padding: 7px 15px;
        color: #ffffff;
        font-size: 18px;
        font-weight: 600;
        border-radius: 5px;
        display: inline-block;
        -moz-box-shadow: 2px 4px 5px 0 #ccc;
        -webkit-box-shadow: 2px 4px 5px 0 #ccc;
        box-shadow: 2px 4px 5px 0 #ccc;
    }

    .total {
        border-bottom: 1px solid #7f8c8d;
        /*display: inline;
    padding: 10px 5px;*/
        position: relative;
        padding-bottom: 20px;
    }

        .total:before {
            content: "";
            display: inline;
            position: absolute;
            left: 0;
            bottom: 5px;
            width: 100%;
            height: 3px;
            background: #7f8c8d;
            opacity: 0.5;
        }

    .price-slider {
        margin-bottom: 70px;
    }

        .price-slider span {
            font-weight: 200;
            display: inline-block;
            color: #7f8c8d;
            font-size: 13px;
        }

    .form-pricing {
        background: #ffffff;
        padding: 20px;
        border-radius: 4px;
    }

    .price-form {
        background: #ffffff;
        margin-bottom: 10px;
        padding: 20px;
        border: 1px solid #eeeeee;
        border-radius: 4px;
        /*-moz-box-shadow:    0 5px 5px 0 #ccc;
    -webkit-box-shadow: 0 5px 5px 0 #ccc;
    box-shadow:         0 5px 5px 0 #ccc;*/
    }

    .form-group {
        margin-bottom: 0;
    }

        .form-group span.price {
            font-weight: 200;
            display: inline-block;
            color: #7f8c8d;
            font-size: 14px;
        }

    .help-text {
        display: block;
        margin-top: 32px;
        margin-bottom: 10px;
        color: #737373;
        position: absolute;
        /*margin-left: 20px;*/
        font-weight: 200;
        text-align: right;
        width: 188px;
    }

    .price-form label {
        font-weight: 200;
        font-size: 21px;
    }

    img.payment {
        display: block;
        margin-left: auto;
        margin-right: auto
    }

    .ui-slider-range-min {
        background: #2980b9;
    }

    /* HR */

    hr.style {
        margin-top: 0;
        border: 0;
        border-bottom: 1px dashed #ccc;
        background: #999;
    }
</style>

<!--@*Slider Control*@-->
<script>
    $(document).ready(function () {
        $("#slider").slider({
            animate: true,
            value: 0,
            min: 0,
            max: 24,
            step: .25,
            slide: function (event, ui) {
                update(1, ui.value); //changed
            }
        });

        $("#slider2").slider({
            animate: true,
            value: 1,
            min: 1,
            max: 10,
            step: 1,
            slide: function (event, ui) {
                update(2, ui.value); //changed
            }
        });

        $("#slider3").slider({
            animate: true,
            value: 0,
            min: 0,
            max: 168,
            step: 1,
            slide: function (event, ui) {
                update(3, ui.value); //changed
            }
        });

        //Added, set initial value.
        $("#amount").val(0);
        $("#duration").val(0);
        $("#frequency").val(0);
        $("#amount-label").text(0);
        $("#duration-label").text(0);
        $("#frequency-label").text(0);

        update();
    });

    //changed. now with parameter
    function update(slider, val) {
        //changed. Now, directly take value from ui.value. if not set (initial, will use current value.)
        var $amount = slider == 1 ? val : $("#amount").val();
        var $duration = slider == 2 ? val : $("#duration").val();
        var $frequency = slider == 3 ? val : $("#frequency").val();

        /* commented
        $amount = $( "#slider" ).slider( "value" );
        $duration = $( "#slider2" ).slider( "value" );
        */

        $total = " " + ($amount * $duration) * $frequency;
        $("#amount").val($amount);
        $("#amount-label").text($amount);
        $("#duration").val($duration);
        $("#duration-label").text($duration);
        $("#frequency").val($frequency);
        $("#frequency-label").text($frequency);
        $("#total").val($total);
        $("#total-label").text($total);

        $('#slider a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $amount + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
        $('#slider2 a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $duration + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
        $('#slider3 a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $frequency + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
    }


</script>

<!--CKEditor Scripts for TextArea Fields *@-->
<script>
    $(function () {
        $('#my-textarea').ckeditor();
    });

</script>

<script>
    $(function () {
        $('#MemoProductNote').ckeditor();
    });

</script>




    @* Cascading DropDown for Product Category*@
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js" type="text/javascript"></script>
   <script type="text/javascript">
    $(function () {
        if ($("#ProdCategoryId").val() == '0') {
            var productDefaultValue = "<option value='0'>--Select a Category first--</option>";
            $("#AvProductId").html(productDefaultValue).show();
        }

        $("#ProdCategoryId").change(function () {
            var selectedItemValue = $(this).val();

            var ddlProducts = $("#AvProductId");
            $.ajax({
                cache: false,
                type: "GET",
                url: '@Url.Action("GetProductsByCategoryId2", "SizingUserDashboard")',
                data: { "id": selectedItemValue },
                success: function (data) {
                    ddlProducts.html('');
                    $.each(data, function (id, option) {
                        ddlProducts.append($('<option></option>').val(option.id).html(option.name));
                    });
                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Found error to load product!!.');
                }
            });
        });
    });
    </script>

    @* Cascading DropDown for Delivery Type *@
    <script type="text/javascript">
    $(function () {
        if ($("#LaborDeliveryTypeId").val() == '0') {
            var typeDefaultValue = "<option value='0'>--Select DeliveryType First--</option>";
            $("#LaborDeliveryId").html(typeDefaultValue).show();
        }

        $("#LaborDeliveryTypeId").change(function () {
            var selectedItemValue = $(this).val();

            var ddlLaborDeliverys = $("#LaborDeliveryId");
            $.ajax({
                cache: false,
                type: "GET",
                url: '@Url.Action("GetLaborDeliveryBySizingTypeId", "SizingUserDashboard")',
                data: { "id": selectedItemValue },
                success: function (data) {
                    ddlLaborDeliverys.html('');
                    $.each(data, function (id, option) {
                        ddlLaborDeliverys.append($('<option></option>').val(option.id).html(option.name));
                    });
                },

                error: function (xhr, ajaxOptions, thrownError) {
                    alert('Found error to load product!!.');
                }
            });
        });

  });





    </script>

//****** Work On Fixing Stuff  ******

   <script type="text/javascript">

        $(function () {
            if ($("#category_ddl").val() == '0') {
                var productDefaultValue = "<option value='0'>--Select a Category first--</option>";
                $("#Product_ddl").html(productDefaultValue).show();
            }

            $("#category_ddl").change(function () {
                var selectedItemValue = $(this).val();

                var ddlProducts = $("#Product_ddl");
                $.ajax({
                    cache: false,
                    type: "GET",
                    url: '/orderitem/ajax_load_products',
                    data: { "id": selectedItemValue },
                    success: function (data) {
                        ddlProducts.html('');
                        $.each(data, function (id, option) {
                            ddlProducts.append($('<option></option>').val(option.id).html(option.name));
                        });
                    },

                    error: function (xhr, ajaxOptions, thrownError) {
                        alert('Found error to load product!!.');
                    }
                });
            });
    });
    </script>